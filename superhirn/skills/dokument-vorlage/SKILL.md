---
name: dokument-vorlage
description: Erstellt wiederkehrende Dokumente wie Angebote, Briefe, Berichte und Aufstellungen aus den Vorlagen von Matthias und Stichpunkten, Mails oder Notizen. Für Meeting-Protokolle den vorhandenen Skill meeting-protokoll nutzen. Nutzen bei "Angebot", "Brief an", "Bericht", "schreib mir ein Dokument für".
---

# Dokument aus Vorlage

## Ablauf

1. Klären, welche Art Dokument es ist. Ist es ein Meeting-Protokoll, an `meeting-protokoll` übergeben.
2. Passende Vorlage im Vorlagenordner suchen (Pfad in `arbeit/CLAUDE.md`). Gibt es keine, fragen, ob eine neue angelegt werden soll, statt frei zu gestalten.
3. Inhalte zusammentragen aus dem, was Matthias mitgibt: Stichpunkte, weitergeleitete Mail, alter Vorgang. Bei Angeboten das letzte Angebot an denselben Kunden als Referenz lesen.
4. Vorlage füllen. Layout, Briefkopf und Schrift der Vorlage bleiben unverändert.
5. Fehlende Angaben als `[???: was fehlt]` markieren und am Ende auflisten.
6. Als Entwurf in `_entwuerfe/` speichern: `JJJJ-MM-TT_<Art>_<Empfänger>.docx`. Auf Wunsch zusätzlich als PDF.

## Text

Humanizer-Regeln aus `CLAUDE.md` gelten auch hier. Angebote und Briefe sind sachlich und knapp, keine Einleitungsfloskeln.

## Danach

Fragen, ob `/mail-entwurf` eine Begleitmail als Entwurf anlegen soll.
