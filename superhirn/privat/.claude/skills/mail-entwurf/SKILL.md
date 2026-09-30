---
name: privat-mail-entwurf
description: Geht ungelesene Mails im privaten Konto durch, filtert Werbung heraus, meldet Preiserhöhungen und Fristen und legt Antwortentwürfe an. Nie senden. Nutzen, wenn Matthias im Privathirn "Postfach", "Mails", "Antwortentwürfe" sagt oder die Abendroutine läuft.
---

# Mail-Entwürfe Privat

## Ablauf

Nur das Werkzeug `mail-privat` verwenden.

1. `mails_suchen(nur_ungelesen=True, seit_tagen=1)`, dann jede relevante Mail mit `mail_lesen` öffnen. Werbung reicht der Betreff.
2. Jede Mail einordnen:
   - Typ: Rechnung, Vertrag/Änderung, Termin, Familie/Freunde, Bestellung/Versand, Newsletter/Werbung, Behörde, Sonstiges
   - Braucht Antwort: ja / nein / Matthias muss entscheiden
   - Beruflich? Dann nicht bearbeiten, nur als „gehört ins Arbeitshirn“ auflisten.
3. Entwürfe nur für Mails mit „ja“, über `entwurf_anlegen(antwort_auf_uid=..., text=...)`. Stil aus dem Humanizer in `CLAUDE.md`, bei Behörden und Firmen „Sie“, bei Familie und Freunden so, wie Matthias es in früheren Mails an die Person gemacht hat. Fehlendes als `[???: was fehlt]`.
4. Preiserhöhungen, Vertragsänderungen und Fristen immer oben melden, mit Betrag und Datum. Mit der Vertragstabelle in `CLAUDE.md` abgleichen.
5. Rechnungsanhänge mit `anhaenge_speichern` in den Scan-Eingang legen, dort greift `/privat-ablage-belege`.
6. Nichts senden, nichts löschen, nichts als gelesen markieren.

## Ausgabe

```
Achtung
- Stadtwerke: Abschlag steigt ab 01.11. von 85 auf 97 €
Entwürfe
- Schwager, Grillen Samstag → Entwurf liegt bereit
Abgelegt vormerken
- Amazon-Rechnung 34,99 €
Werbung / nur Info: 12 Mails
Nicht meins: 1 Kundenmail → Arbeitshirn
```
