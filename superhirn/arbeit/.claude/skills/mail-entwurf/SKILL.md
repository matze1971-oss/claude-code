---
name: arbeit-mail-entwurf
description: Geht ungelesene Mails im Arbeitskonto durch, sortiert sie nach Dringlichkeit und legt für Standardfälle Antwortentwürfe an, im Ton von Matthias. Nie senden. Nutzen, wenn Matthias im Arbeitshirn "Postfach", "Mails abarbeiten", "Antwortentwürfe" sagt oder die Morgenroutine läuft.
---

# Mail-Entwürfe Arbeit

## Ablauf

Nur das Werkzeug `mail-arbeit` verwenden.

1. `mails_suchen(nur_ungelesen=True, seit_tagen=<seit letztem Werktag>)`, dann jede Mail mit `mail_lesen` öffnen. Beides ändert nichts am Gelesen-Status.
2. Jede Mail einordnen:
   - Typ: Termin, Rückfrage, Angebot/Auftrag, Rechnung, Info, Newsletter, Sonstiges
   - Braucht Antwort: ja / nein / Matthias muss entscheiden
   - Privat? Dann nicht bearbeiten, nur als „gehört ins Privathirn“ auflisten.
3. Für jede Mail mit „ja“ `entwurf_anlegen(antwort_auf_uid=..., text=...)`. Empfänger, Betreff und Verlauf übernimmt das Werkzeug. Regeln für den Text:
   - Ansprache aus der Kundentabelle, Stil aus dem Humanizer in `CLAUDE.md`
   - Nur Fakten aus Mail, Thread oder Arbeitsordner. Fehlt etwas (Termin, Preis, Zusage), `[???: was fehlt]` setzen, nichts erfinden.
   - Kurz. Meist drei bis sechs Sätze.
4. Rechnungen nicht beantworten. Anhänge mit `anhaenge_speichern` in den Beleg-Eingang legen, dort greift `/arbeit-ablage-belege`.
5. Nichts senden, nichts löschen, nichts als gelesen markieren.

## Ausgabe

Kurze Übersicht, „muss heute raus“ zuerst:

```
- Kunde A, Terminanfrage → Entwurf liegt bereit (1 Platzhalter: Uhrzeit)
- Lieferant X, Rechnung → für Ablage vorgemerkt
- Kunde B will Rabatt → kein Entwurf, bitte Vorgabe
Nicht meins: 1 private Mail (Paketdienst) → Privathirn
```

## Aus Korrekturen lernen

Ändert Matthias einen Entwurf auf eine Art, die schon einmal vorkam, eine neue Regel für `CLAUDE.md` vorschlagen.
