"""Superhirn Mail-Baustein.

Kleiner MCP-Server, der ein IMAP-Postfach für Claude lesbar macht und
Entwürfe in den Entwürfe-Ordner legen kann. Senden, löschen oder als
gelesen markieren kann er nicht, weil es dafür keine Funktion gibt.

Pro Hirn läuft eine eigene Instanz mit eigenem Konto. Einstellungen kommen
aus Umgebungsvariablen (siehe README.md), das Passwort aus der Windows-
Anmeldeinformationsverwaltung.
"""

from __future__ import annotations

import email
import email.policy
import html
import imaplib
import os
import re
import time
from contextlib import contextmanager
from datetime import date, timedelta
from email.message import EmailMessage
from email.utils import formatdate, getaddresses, make_msgid, parsedate_to_datetime
from pathlib import Path

from mcp.server.mcpserver import MCPServer

KEYRING_DIENST = "superhirn-mail"
MONATE = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MAX_TEXT = 20000
MAX_TREFFER = 100

# Übliche Ordnernamen, falls der Server keine SPECIAL-USE-Kennung liefert
NAMEN_GESENDET = ["Sent", "Gesendet", "Gesendete Objekte", "Gesendete Elemente", "Sent Items",
                  "Sent Messages", "INBOX.Sent", "INBOX.Gesendet", "INBOX/Sent"]
NAMEN_ENTWUERFE = ["Drafts", "Entwürfe", "Entwurf", "INBOX.Drafts", "INBOX.Entwürfe", "INBOX/Drafts"]

KONTO = os.environ.get("SUPERHIRN_KONTO", "mail")

mcp = MCPServer(
    name=f"superhirn-mail-{KONTO}",
    instructions=(
        f"Postfach für das Hirn '{KONTO}'. Nur benutzen, wenn du im Hirn '{KONTO}' arbeitest. "
        "Lesen verändert nichts am Postfach. Antworten werden nur als Entwurf abgelegt; "
        "Senden, Löschen und Markieren sind nicht möglich."
    ),
)


# ---------------------------------------------------------------- Einstellungen

def _einstellung(name: str, standard: str | None = None) -> str:
    wert = os.environ.get(name, standard)
    if not wert:
        raise RuntimeError(f"Einstellung {name} fehlt in der Konfiguration.")
    return wert


def _passwort(benutzer: str) -> str:
    # Nur für Tests. Im Alltag liegt das Passwort in der Anmeldeinformationsverwaltung.
    if os.environ.get("IMAP_PASSWORT"):
        return os.environ["IMAP_PASSWORT"]
    import keyring

    pw = keyring.get_password(KEYRING_DIENST, benutzer)
    if not pw:
        raise RuntimeError(
            f"Kein Passwort für {benutzer} gespeichert. Einmal ausführen: "
            f"python passwort_speichern.py {benutzer}"
        )
    return pw


@contextmanager
def _verbindung():
    host = _einstellung("IMAP_HOST")
    sicherheit = os.environ.get("IMAP_SICHERHEIT", "ssl").lower()
    benutzer = _einstellung("IMAP_USER")
    if sicherheit == "ssl":
        conn = imaplib.IMAP4_SSL(host, int(os.environ.get("IMAP_PORT", "993")))
    else:
        conn = imaplib.IMAP4(host, int(os.environ.get("IMAP_PORT", "143")))
        if sicherheit == "starttls":
            conn.starttls()
        elif sicherheit != "keine":
            raise RuntimeError("IMAP_SICHERHEIT muss ssl, starttls oder keine sein.")
    try:
        conn.login(benutzer, _passwort(benutzer))
        yield conn
    finally:
        try:
            conn.logout()
        except Exception:
            pass


# ---------------------------------------------------------------- Ordner

_LIST_ZEILE = re.compile(r'\((?P<flags>[^)]*)\) (?P<trenner>"[^"]*"|NIL) (?P<name>.+)')


def _utf7_dekodieren(name: str) -> str:
    """IMAP-Ordnernamen (modifiziertes UTF-7, RFC 3501) lesbar machen."""
    def ersetzen(m: re.Match) -> str:
        teil = m.group(1)
        if not teil:
            return "&"
        b64 = teil.replace(",", "/")
        b64 += "=" * (-len(b64) % 4)
        import base64
        return base64.b64decode(b64).decode("utf-16-be")
    return re.sub(r"&([^-]*)-", ersetzen, name)


def _ordner_liste(conn) -> list[dict]:
    typ, daten = conn.list()
    ergebnis = []
    for zeile in daten or []:
        if not zeile:
            continue
        text = zeile.decode("utf-8", "replace") if isinstance(zeile, bytes) else str(zeile)
        m = _LIST_ZEILE.match(text)
        if not m:
            continue
        roh = m.group("name").strip()
        ohne = roh[1:-1] if roh.startswith('"') and roh.endswith('"') else roh
        ergebnis.append({
            "roh": ohne,
            "name": _utf7_dekodieren(ohne),
            "flags": m.group("flags").split(),
        })
    return ergebnis


def _ordner_finden(conn, wunsch: str) -> str:
    """'posteingang', 'gesendet', 'entwuerfe' oder ein echter Ordnername -> Name für SELECT."""
    w = wunsch.strip().lower()
    if w in ("posteingang", "inbox", "eingang"):
        return "INBOX"
    liste = _ordner_liste(conn)
    for kennung, namen, stichwort, env in (
        ("\\Sent", NAMEN_GESENDET, ("gesendet", "sent"), "IMAP_ORDNER_GESENDET"),
        ("\\Drafts", NAMEN_ENTWUERFE, ("entwuerfe", "entwürfe", "drafts"), "IMAP_ORDNER_ENTWUERFE"),
    ):
        if w in stichwort:
            if os.environ.get(env):
                return os.environ[env]
            for o in liste:
                if kennung in o["flags"]:
                    return o["roh"]
            for n in namen:
                for o in liste:
                    if o["name"].lower() == n.lower():
                        return o["roh"]
            raise RuntimeError(f"Ordner '{wunsch}' nicht gefunden. In der Konfiguration {env} setzen.")
    for o in liste:
        if o["name"].lower() == w or o["roh"].lower() == w:
            return o["roh"]
    raise RuntimeError(f"Ordner '{wunsch}' gibt es nicht. ordner_auflisten zeigt alle.")


def _quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _lesend_oeffnen(conn, ordner: str) -> str:
    name = _ordner_finden(conn, ordner)
    typ, daten = conn.select(_quote(name), readonly=True)  # EXAMINE: ändert keine Flags
    if typ != "OK":
        raise RuntimeError(f"Ordner '{ordner}' lässt sich nicht öffnen: {daten}")
    return name


# ---------------------------------------------------------------- Nachrichten

def _kopf(msg, feld: str) -> str:
    wert = msg.get(feld)
    return str(wert) if wert is not None else ""


def _datum_iso(msg) -> str:
    try:
        return parsedate_to_datetime(_kopf(msg, "Date")).isoformat(timespec="minutes")
    except Exception:
        return _kopf(msg, "Date")


def _text_aus(msg) -> str:
    teil = msg.get_body(preferencelist=("plain", "html"))
    if teil is None:
        return ""
    try:
        inhalt = teil.get_content()
    except Exception:
        inhalt = teil.get_payload(decode=True).decode("utf-8", "replace")
    if teil.get_content_subtype() == "html":
        inhalt = re.sub(r"(?is)<(script|style).*?</\1>", "", inhalt)
        inhalt = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", inhalt)
        inhalt = html.unescape(re.sub(r"<[^>]+>", "", inhalt))
    inhalt = inhalt.replace("\r\n", "\n")
    inhalt = re.sub(r"\n{3,}", "\n\n", inhalt).strip()
    return inhalt


def _anhaenge(msg) -> list:
    return [t for t in msg.iter_attachments() if t.get_filename()]


def _nachricht_holen(conn, uid: str):
    typ, daten = conn.uid("FETCH", uid, "(BODY.PEEK[])")
    for teil in daten or []:
        if isinstance(teil, tuple):
            return email.message_from_bytes(teil[1], policy=email.policy.default)
    raise RuntimeError(f"Mail {uid} nicht gefunden.")


def _imap_datum(tage: int) -> str:
    d = date.today() - timedelta(days=max(tage, 0))
    return f"{d.day:02d}-{MONATE[d.month - 1]}-{d.year}"


# ---------------------------------------------------------------- Werkzeuge

@mcp.tool()
def ordner_auflisten() -> list[dict]:
    """Zeigt alle Ordner des Postfachs mit Kennzeichnung (z. B. Gesendet, Entwürfe)."""
    with _verbindung() as conn:
        return [{"name": o["name"], "kennung": [f for f in o["flags"] if f in
                 ("\\Sent", "\\Drafts", "\\Trash", "\\Junk", "\\Archive")]} for o in _ordner_liste(conn)]


@mcp.tool()
def mails_suchen(
    ordner: str = "posteingang",
    seit_tagen: int = 1,
    nur_ungelesen: bool = False,
    von: str | None = None,
    an: str | None = None,
    betreff: str | None = None,
    volltext: str | None = None,
    max_anzahl: int = 30,
) -> list[dict]:
    """Sucht Mails und liefert Kopfdaten (uid, von, an, betreff, datum, ungelesen), neueste zuerst.

    ordner: 'posteingang', 'gesendet', 'entwuerfe' oder ein Name aus ordner_auflisten.
    seit_tagen: 0 = heute, 1 = seit gestern, 60 = letzte zwei Monate.
    von / an / betreff / volltext: Teil des Textes, Groß-/Kleinschreibung egal.
    Die Suche verändert nichts, auch ungelesene Mails bleiben ungelesen.
    """
    max_anzahl = max(1, min(max_anzahl, MAX_TREFFER))
    with _verbindung() as conn:
        _lesend_oeffnen(conn, ordner)
        kriterien: list[str] = ["SINCE", _imap_datum(seit_tagen)]
        if nur_ungelesen:
            kriterien.append("UNSEEN")
        nachfilter = {}
        for feld, wert in (("FROM", von), ("TO", an), ("SUBJECT", betreff)):
            if not wert:
                continue
            if wert.isascii():
                kriterien += [feld, _quote(wert)]
            else:
                nachfilter[feld] = wert.lower()
        if volltext and not volltext.isascii():
            conn.literal = volltext.encode("utf-8")
            typ, daten = conn.uid("SEARCH", "CHARSET", "UTF-8", *kriterien, "TEXT")
        else:
            if volltext:
                kriterien += ["TEXT", _quote(volltext)]
            typ, daten = conn.uid("SEARCH", *kriterien)
        uids = (daten[0] or b"").split() if daten else []
        uids = list(reversed(uids))[: max_anzahl * (4 if nachfilter else 1)]
        if not uids:
            return []

        typ, daten = conn.uid(
            "FETCH", b",".join(uids).decode(),
            "(UID FLAGS BODY.PEEK[HEADER.FIELDS (FROM TO CC SUBJECT DATE)])",
        )
        treffer = []
        for teil in daten or []:
            if not isinstance(teil, tuple):
                continue
            meta = teil[0].decode("ascii", "replace")
            uid = re.search(r"UID (\d+)", meta)
            msg = email.message_from_bytes(teil[1], policy=email.policy.default)
            eintrag = {
                "uid": uid.group(1) if uid else "",
                "von": _kopf(msg, "From"),
                "an": _kopf(msg, "To"),
                "betreff": _kopf(msg, "Subject"),
                "datum": _datum_iso(msg),
                "ungelesen": "\\Seen" not in meta,
            }
            if all(w in eintrag[{"FROM": "von", "TO": "an", "SUBJECT": "betreff"}[f]].lower()
                   for f, w in nachfilter.items()):
                treffer.append(eintrag)
        treffer.sort(key=lambda e: int(e["uid"] or 0), reverse=True)
        return treffer[:max_anzahl]


@mcp.tool()
def mail_lesen(uid: str, ordner: str = "posteingang") -> dict:
    """Liest eine Mail komplett: Kopfdaten, Text und Liste der Anhänge. Markiert nichts als gelesen."""
    with _verbindung() as conn:
        _lesend_oeffnen(conn, ordner)
        msg = _nachricht_holen(conn, uid)
        text = _text_aus(msg)
        return {
            "uid": uid,
            "von": _kopf(msg, "From"),
            "antwort_an": _kopf(msg, "Reply-To"),
            "an": _kopf(msg, "To"),
            "cc": _kopf(msg, "Cc"),
            "betreff": _kopf(msg, "Subject"),
            "datum": _datum_iso(msg),
            "message_id": _kopf(msg, "Message-ID"),
            "text": text[:MAX_TEXT] + ("\n[… gekürzt]" if len(text) > MAX_TEXT else ""),
            "anhaenge": [{"datei": t.get_filename(), "typ": t.get_content_type(),
                          "groesse_kb": round(len(t.get_payload(decode=True) or b"") / 1024)}
                         for t in _anhaenge(msg)],
        }


@mcp.tool()
def entwurf_anlegen(
    text: str,
    an: str | None = None,
    betreff: str | None = None,
    cc: str | None = None,
    antwort_auf_uid: str | None = None,
    antwort_ordner: str = "posteingang",
    original_zitieren: bool = True,
) -> dict:
    """Legt eine Mail als Entwurf in den Entwürfe-Ordner. Sie wird NICHT gesendet.

    Als Antwort: antwort_auf_uid angeben. Empfänger, Betreff (mit 'AW:') und Verlauf
    werden dann aus der Originalmail übernommen, an/betreff überschreiben das nur,
    wenn sie gesetzt sind. Der Entwurf erscheint in Outlook im Ordner Entwürfe.
    """
    absender = os.environ.get("IMAP_ABSENDER") or _einstellung("IMAP_USER")
    neu = EmailMessage()
    neu["From"] = absender
    neu["Date"] = formatdate(localtime=True)
    neu["Message-ID"] = make_msgid(domain=absender.split("@")[-1].strip(">") if "@" in absender else None)
    neu["X-Superhirn"] = f"Entwurf {KONTO}"
    koerper = text.rstrip() + "\n"

    with _verbindung() as conn:
        if antwort_auf_uid:
            _lesend_oeffnen(conn, antwort_ordner)
            orig = _nachricht_holen(conn, antwort_auf_uid)
            orig_betreff = _kopf(orig, "Subject")
            if not betreff:
                betreff = orig_betreff if re.match(r"(?i)^(aw|re|antw)\s*:", orig_betreff) else f"AW: {orig_betreff}"
            if not an:
                an = _kopf(orig, "Reply-To") or _kopf(orig, "From")
            mid = _kopf(orig, "Message-ID")
            if mid:
                neu["In-Reply-To"] = mid
                neu["References"] = (_kopf(orig, "References") + " " + mid).strip()
            if original_zitieren:
                koerper += (
                    "\n\n-----Ursprüngliche Nachricht-----\n"
                    f"Von: {_kopf(orig, 'From')}\n"
                    f"Gesendet: {_kopf(orig, 'Date')}\n"
                    f"An: {_kopf(orig, 'To')}\n"
                    f"Betreff: {orig_betreff}\n\n"
                    + _text_aus(orig)
                )
        if not an:
            raise RuntimeError("Kein Empfänger. 'an' angeben oder antwort_auf_uid nutzen.")
        neu["To"] = an
        if cc:
            neu["Cc"] = cc
        neu["Subject"] = betreff or ""
        neu.set_content(koerper)

        ziel = _ordner_finden(conn, "entwuerfe")
        typ, daten = conn.append(_quote(ziel), "(\\Draft \\Seen)",
                                 imaplib.Time2Internaldate(time.time()), neu.as_bytes())
        if typ != "OK":
            raise RuntimeError(f"Entwurf konnte nicht abgelegt werden: {daten}")
        return {"ok": True, "ordner": _utf7_dekodieren(ziel), "an": an, "betreff": neu["Subject"]}


_UNERLAUBT = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


@mcp.tool()
def anhaenge_speichern(uid: str, ordner: str = "posteingang") -> dict:
    """Speichert die Anhänge einer Mail in den Anhang-Eingang dieses Hirns.

    Dateiname: JJJJ-MM-TT_<Originalname>. Vorhandene Dateien werden nie überschrieben.
    """
    ziel = Path(_einstellung("ANHANG_ORDNER"))
    ziel.mkdir(parents=True, exist_ok=True)
    with _verbindung() as conn:
        _lesend_oeffnen(conn, ordner)
        msg = _nachricht_holen(conn, uid)
        try:
            tag = parsedate_to_datetime(_kopf(msg, "Date")).date().isoformat()
        except Exception:
            tag = date.today().isoformat()
        gespeichert = []
        for t in _anhaenge(msg):
            # Pfadtrenner werden zu "_", damit nichts außerhalb des Ordners landet
            name = _UNERLAUBT.sub("_", t.get_filename()).strip(" .") or "anhang"
            pfad = ziel / f"{tag}_{name}"
            n = 2
            while pfad.exists():
                pfad = ziel / f"{tag}_{Path(name).stem}_{n}{Path(name).suffix}"
                n += 1
            pfad.write_bytes(t.get_payload(decode=True) or b"")
            gespeichert.append(str(pfad))
        return {"gespeichert": gespeichert}


if __name__ == "__main__":
    mcp.run()
