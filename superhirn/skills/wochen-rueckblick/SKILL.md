---
name: wochen-rueckblick
description: Wertet das Aktivitätsprotokoll, das Ablage-Log und die Mails der Woche aus, findet Aufgaben, die sich wiederholen, und schlägt neue Automatisierungen oder Regeln vor. Nutzen bei "Wochenrückblick", "was wiederholt sich", "was kann ich automatisieren" oder freitags per Routine.
---

# Wochenrückblick

## Quellen

- `protokoll/aktivitaet.csv` (Zeit, Ereignis, Ordner, Datei) der letzten 7 Tage
- `protokoll/ablage.log`
- Gesendete Mails der letzten 7 Tage (nur Betreff, Empfänger und die ersten Zeilen)
- Entwürfe, die Matthias vor dem Senden deutlich geändert hat

## Wonach suchen

- Dateien, die immer wieder im selben Muster entstehen oder verschoben werden (z. B. jeden Montag ein Export aus demselben Programm)
- Mails, die Matthias mehrmals fast gleich geschrieben hat
- Ordner, in denen sich Dateien ansammeln, ohne abgelegt zu werden
- Korrekturen an Entwürfen, die sich wiederholen

Einzelne Ereignisse zählen nicht. Ein Muster braucht mindestens drei Vorkommen in der Woche oder zwei Wochen in Folge.

## Ausgabe

Kurz und ehrlich. Höchstens fünf Vorschläge, sortiert nach geschätzter Zeitersparnis pro Monat:

```
1. Monatsexport aus [Programm] → Downloads → händisch nach Kunden/…
   Gesehen: 4x diese Woche, je ca. 5 Min.
   Vorschlag: Regel in ablage-belege ergänzen
   Ersparnis: ca. 1 Std./Monat
```

Wenn es nichts Neues gibt, das so sagen. Keine Vorschläge erfinden, um die Liste zu füllen.

Vertrauliche Kunden und Tabu-Themen aus den Bereichs-Dateien nicht nennen.
