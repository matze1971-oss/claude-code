---
name: arbeit-wochen-rueckblick
description: Wertet das Aktivitätsprotokoll, das Ablage-Log und die gesendeten Mails der Arbeitswoche aus, findet Aufgaben, die sich wiederholen, und schlägt Automatisierungen oder neue Regeln vor. Nutzen bei "Wochenrückblick", "was wiederholt sich", "was kann ich automatisieren" im Arbeitshirn oder freitags per Routine.
---

# Wochenrückblick Arbeit

## Quellen

- `protokoll/aktivitaet.csv` der letzten 7 Tage
- `protokoll/ablage.log`
- Gesendete Mails der letzten 7 Tage über `mail-arbeit`: `mails_suchen(ordner="gesendet", seit_tagen=7)`
- Entwürfe, die Matthias vor dem Senden deutlich geändert hat

## Wonach suchen

- Dateien, die immer im selben Muster entstehen oder verschoben werden (z. B. jeden Montag ein Export aus demselben Programm)
- Mails, die Matthias mehrmals fast gleich geschrieben hat
- Ordner, in denen sich Dateien ansammeln
- Korrekturen an Entwürfen, die sich wiederholen

Ein Muster braucht mindestens drei Vorkommen in der Woche oder zwei Wochen in Folge.

## Ausgabe

Höchstens fünf Vorschläge, sortiert nach geschätzter Zeitersparnis pro Monat:

```
1. Monatsexport aus [Programm] → Downloads → händisch nach Kunden/…
   Gesehen: 4x, je ca. 5 Min.
   Vorschlag: Regel in arbeit-ablage-belege ergänzen
   Ersparnis: ca. 1 Std./Monat
```

Gibt es nichts Neues, das so sagen. Keine Vorschläge erfinden. Vertrauliche Kunden aus `CLAUDE.md` nicht nennen.
