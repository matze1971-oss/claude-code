---
name: ablage-belege
description: Liest neue PDFs, Scans und Rechnungen aus Downloads, Scan-Eingang und Mail-Anhängen, erkennt Absender, Datum, Art und Betrag und schlägt Dateinamen und Zielordner nach dem Ablageplan vor. Verschiebt erst nach Freigabe. Nutzen bei "ablegen", "Belege", "Rechnungen sortieren", "Downloads aufräumen" oder in der Abendroutine.
---

# Ablage und Belege

## Ablauf

1. Quellen durchsehen: Downloads, Scan-Eingang (Pfad in `privat/CLAUDE.md`), Beleg-Eingang Arbeit (Pfad in `arbeit/CLAUDE.md`), dazu Mails, die `/mail-entwurf` als Rechnung vorgemerkt hat.
2. Jede Datei lesen. Gescannte PDFs ohne Text vorher per OCR lesbar machen.
3. Herausziehen: Datum auf dem Beleg, Absender, Art (Rechnung, Vertrag, Bescheid, Angebot, Sonstiges), Betrag, Bereich (Arbeit/Privat).
4. Dateinamen und Zielordner nach dem Ablageplan des Bereichs bilden.
5. Unsicher ist alles, wo Bereich oder Absender nicht eindeutig sind. Diese Dateien nicht raten, sondern gesondert auflisten.

## Ausgabe

Eine Tabelle zur Freigabe:

| # | Datei jetzt | Neuer Name | Zielordner | Steuer? |
|---|---|---|---|---|
| 1 | scan0042.pdf | 2026-09-28_Stadtwerke_Rechnung_112,40.pdf | Privat/Haus/2026 | nein |

Darunter: „Unklar“ mit Grund.

Matthias antwortet z. B. „alle außer 3“ oder „ok“. Erst dann verschieben und umbenennen. Vorhandene Dateien nie überschreiben, bei gleichem Namen `_2` anhängen.

Nach dem Verschieben eine Zeile pro Datei in `protokoll/ablage.log` schreiben (Datum, alter Pfad, neuer Pfad), damit sich alles zurückverfolgen lässt.
