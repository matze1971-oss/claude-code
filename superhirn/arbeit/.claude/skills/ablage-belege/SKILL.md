---
name: arbeit-ablage-belege
description: Liest neue Rechnungen, PDFs und Scans aus dem Beleg-Eingang Arbeit und vorgemerkten Mail-Anhängen, erkennt Absender, Datum, Art und Betrag und schlägt Dateinamen und Zielordner nach dem Ablageplan Arbeit vor. Verschiebt erst nach Freigabe. Nutzen bei "ablegen", "Belege", "Rechnungen sortieren" im Arbeitshirn oder in der Abendroutine.
---

# Ablage und Belege Arbeit

## Ablauf

1. Quelle: Beleg-Eingang Arbeit (Pfad in `CLAUDE.md`). Rechnungsanhänge aus Mails landen dort über den Mail-Baustein automatisch.
2. Jede Datei lesen. Gescannte PDFs ohne Text vorher per OCR lesbar machen.
3. Herausziehen: Datum auf dem Beleg, Absender, Art (Rechnung, Angebot, Vertrag, Lieferschein, Sonstiges), Betrag, Kunde oder Projekt.
4. Dateinamen und Zielordner nach dem Ablageplan in `CLAUDE.md` bilden.
5. Private Belege nicht einsortieren, nur als „gehört ins Privathirn“ auflisten.
6. Wo Kunde oder Absender nicht eindeutig sind, nicht raten, sondern unter „Unklar“ auflisten.

## Ausgabe

| # | Datei jetzt | Neuer Name | Zielordner |
|---|---|---|---|
| 1 | scan0042.pdf | 2026-09-28_Lieferant-X_Rechnung_412,40.pdf | Rechnungen/2026/09 |

Darunter „Unklar“ und „Nicht meins“, jeweils mit Grund.

Erst nach Freigabe („ok“, „alle außer 3“) verschieben und umbenennen. Nie überschreiben, bei gleichem Namen `_2` anhängen. Danach eine Zeile pro Datei in `protokoll/ablage.log` (Datum; alter Pfad; neuer Pfad).
