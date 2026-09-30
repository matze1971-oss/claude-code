---
name: privat-wochen-rueckblick
description: Wertet das private Aktivitätsprotokoll, das Ablage-Log und die gesendeten privaten Mails aus, zeigt anstehende Fristen und schlägt Automatisierungen vor. Nutzen bei "Wochenrückblick", "was steht an", "was wiederholt sich" im Privathirn oder samstags per Routine.
---

# Wochenrückblick Privat

## Quellen

- `protokoll/aktivitaet.csv` der letzten 7 Tage
- `protokoll/ablage.log`
- Gesendete Mails der letzten 7 Tage über `mail-privat`: `mails_suchen(ordner="gesendet", seit_tagen=7)`
- Vertragstabelle in `CLAUDE.md`

## Inhalt

Zuerst Fristen: Kündigungsfristen und Zahlungen, die in den nächsten 30 Tagen anstehen.

Dann Muster, mindestens drei Vorkommen in der Woche oder zwei Wochen in Folge:
- Dateien, die sich im Download- oder Scan-Ordner ansammeln
- Mails, die Matthias mehrmals ähnlich geschrieben hat
- Wiederkehrende Aufgaben, z. B. monatlich dieselbe Überweisung prüfen

Höchstens fünf Vorschläge mit geschätzter Zeitersparnis. Gibt es nichts Neues, das so sagen. Tabu-Themen aus `CLAUDE.md` nicht nennen.
