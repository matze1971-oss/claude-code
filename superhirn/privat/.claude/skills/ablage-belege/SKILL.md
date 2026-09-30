---
name: privat-ablage-belege
description: Liest neue private PDFs, Scans und Rechnungen aus Downloads, Scan-Eingang und vorgemerkten Mail-Anhängen, schlägt Dateinamen und Zielordner nach dem Ablageplan Privat vor und markiert steuerrelevante Belege. Verschiebt erst nach Freigabe. Nutzen bei "ablegen", "Belege", "Scans sortieren", "Steuer" im Privathirn.
---

# Ablage und Belege Privat

## Ablauf

1. Quellen: Downloads und Scan-Eingang (Pfad in `CLAUDE.md`). Rechnungsanhänge aus Mails landen über den Mail-Baustein im Scan-Eingang.
2. Jede Datei lesen, Scans ohne Text vorher per OCR lesbar machen.
3. Herausziehen: Datum, Absender, Art (Rechnung, Vertrag, Bescheid, Versicherung, Arzt, Sonstiges), Betrag.
4. Dateinamen und Zielordner nach dem Ablageplan in `CLAUDE.md` bilden.
5. Steuerrelevant? Kategorie aus `CLAUDE.md` vorschlagen.
6. Berufliche Belege nicht einsortieren, nur als „gehört ins Arbeitshirn“ auflisten.
7. Unklares nicht raten, sondern gesondert auflisten.

## Ausgabe

| # | Datei jetzt | Neuer Name | Zielordner | Steuer |
|---|---|---|---|---|
| 1 | scan0042.pdf | 2026-09-28_Stadtwerke_Rechnung.pdf | Haus/2026 | – |
| 2 | Rechnung_8812.pdf | 2026-09-20_Elektro-Maier_Rechnung.pdf | Haus/2026 | Handwerker, 380,00 € |

Darunter „Unklar“ und „Nicht meins“ mit Grund.

Erst nach Freigabe verschieben, umbenennen und Steuer-Einträge schreiben. Nie überschreiben, bei gleichem Namen `_2` anhängen. Danach eine Zeile pro Datei in `protokoll/ablage.log`.
