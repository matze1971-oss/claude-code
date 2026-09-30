---
name: mail-entwurf
description: Geht ungelesene oder markierte Mails durch, sortiert sie nach Arbeit/Privat und Dringlichkeit und legt für Standardfälle Antwortentwürfe in Gmail an, im Ton von Matthias. Nie senden. Nutzen, wenn Matthias "Postfach", "Mails abarbeiten", "Antwortentwürfe" sagt oder die Morgenroutine läuft.
---

# Mail-Entwürfe

## Ablauf

1. Mails holen. Standard: ungelesen im Posteingang seit dem letzten Werktag. Hat Matthias etwas anderes gesagt, das nehmen.
2. Jede Mail einordnen:
   - Bereich: Arbeit oder Privat (nach Absender und Inhalt, Regeln aus `arbeit/CLAUDE.md` und `privat/CLAUDE.md`)
   - Typ: Termin, Rückfrage, Angebot/Auftrag, Rechnung, Info, Newsletter, Sonstiges
   - Braucht Antwort: ja / nein / Matthias muss entscheiden
3. Für jede Mail mit „ja“ einen Entwurf als Antwort im Thread anlegen. Regeln:
   - Ton und Ansprache aus der Kundentabelle bzw. dem Humanizer in `CLAUDE.md`
   - Nur Fakten verwenden, die in der Mail, im Thread oder in den Dateien stehen. Fehlt etwas (Termin, Preis, Zusage), Platzhalter `[???: was fehlt]` setzen, nicht erfinden.
   - Kurz. Die meisten Antworten sind drei bis sechs Sätze.
4. Rechnungen nicht beantworten, sondern für `/ablage-belege` vormerken.
5. Nichts senden, nichts löschen, nichts als gelesen markieren.

## Ausgabe an Matthias

Eine kurze Übersicht, sortiert nach „muss heute raus“ zuerst:

```
Arbeit
- Kunde A, Terminanfrage → Entwurf liegt bereit (1 Platzhalter: Uhrzeit)
- Lieferant X, Rechnung → für Ablage vorgemerkt
Privat
- Versicherung, Beitragsanpassung → keine Antwort nötig, Info: +4,20 €/Monat ab 01.11.
Deine Entscheidung
- Kunde B will Rabatt → kein Entwurf, bitte Vorgabe
```

## Aus Korrekturen lernen

Wenn Matthias einen Entwurf ändert und das Muster schon einmal vorkam, eine neue Regel für die passende `CLAUDE.md` vorschlagen.
