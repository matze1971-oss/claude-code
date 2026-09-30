---
name: arbeit-mail-entwurf
description: Geht ungelesene Mails im Arbeitskonto durch, sortiert sie nach Dringlichkeit und legt für Standardfälle Antwortentwürfe an, im Ton von Matthias. Nie senden. Nutzen, wenn Matthias im Arbeitshirn "Postfach", "Mails abarbeiten", "Antwortentwürfe" sagt oder die Morgenroutine läuft.
---

# Mail-Entwürfe Arbeit

## Ablauf

1. Mails aus dem Arbeitskonto holen (Adresse in `CLAUDE.md`). Standard: ungelesen im Posteingang seit dem letzten Werktag.
2. Jede Mail einordnen:
   - Typ: Termin, Rückfrage, Angebot/Auftrag, Rechnung, Info, Newsletter, Sonstiges
   - Braucht Antwort: ja / nein / Matthias muss entscheiden
   - Privat? Dann nicht bearbeiten, nur als „gehört ins Privathirn“ auflisten.
3. Für jede Mail mit „ja“ einen Entwurf als Antwort im Thread anlegen:
   - Ansprache aus der Kundentabelle, Stil aus dem Humanizer in `CLAUDE.md`
   - Nur Fakten aus Mail, Thread oder Arbeitsordner. Fehlt etwas (Termin, Preis, Zusage), `[???: was fehlt]` setzen, nichts erfinden.
   - Kurz. Meist drei bis sechs Sätze.
4. Rechnungen nicht beantworten, sondern für `/arbeit-ablage-belege` vormerken.
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
