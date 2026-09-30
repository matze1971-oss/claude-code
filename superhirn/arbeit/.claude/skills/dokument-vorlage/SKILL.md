---
name: arbeit-dokument-vorlage
description: Erstellt wiederkehrende berufliche Dokumente wie Angebote, Briefe, Berichte und Aufstellungen aus den Vorlagen von Matthias und Stichpunkten, Mails oder Notizen. Für Meeting-Protokolle den Skill meeting-protokoll nutzen. Nutzen bei "Angebot", "Brief an", "Bericht", "Dokument für" im Arbeitshirn.
---

# Dokument aus Vorlage

## Ablauf

1. Art des Dokuments klären. Meeting-Protokoll → an `meeting-protokoll` übergeben.
2. Passende Vorlage im Vorlagenordner suchen (Pfad in `CLAUDE.md`). Gibt es keine, fragen, ob eine angelegt werden soll, statt frei zu gestalten.
3. Inhalte zusammentragen: Stichpunkte, weitergeleitete Mail, alter Vorgang. Bei Angeboten das letzte Angebot an denselben Kunden als Referenz lesen.
4. Vorlage füllen. Layout, Briefkopf und Schrift bleiben unverändert.
5. Fehlende Angaben als `[???: was fehlt]` markieren und am Ende auflisten.
6. Als Entwurf in `_entwuerfe/` speichern: `JJJJ-MM-TT_<Art>_<Empfänger>.docx`, auf Wunsch zusätzlich PDF.

Humanizer-Regeln aus `CLAUDE.md` gelten auch hier. Sachlich, knapp, keine Einleitungsfloskeln.

Danach fragen, ob `/arbeit-mail-entwurf` eine Begleitmail als Entwurf anlegen soll.
