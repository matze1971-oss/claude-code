# Superhirn

Startpaket für Matthias. Ein Gedächtnis, zwei Bereiche (Arbeit und Privat), vier Skills und ein leichtes Protokoll, das zeigt, was sich wiederholt.

Grundregel: Das Superhirn bereitet vor, du entscheidest. Es schreibt Entwürfe, schlägt Dateinamen vor und legt nichts ab und verschickt nichts, ohne dass du es freigibst.

## Aufbau

```
Superhirn/
  CLAUDE.md                 Gedächtnis: wer du bist, wie du schreibst, was erlaubt ist
  arbeit/CLAUDE.md          Kunden, Projekte, Ablageplan Arbeit
  privat/CLAUDE.md          Haushalt, Verträge, Ablageplan Privat
  skills/                   Rezepte für wiederkehrende Aufgaben
    mail-entwurf/
    ablage-belege/
    dokument-vorlage/
    wochen-rueckblick/
  protokoll/
    beobachter.ps1          schreibt mit, welche Dateien du anfasst
    aktivitaet.csv          entsteht automatisch
```

## Einrichten (einmal, ca. 30 Minuten)

1. Den Ordner `superhirn` nach `C:\Superhirn` kopieren. Deine echten Arbeits- und Privatordner bleiben, wo sie sind. In `arbeit/CLAUDE.md` und `privat/CLAUDE.md` trägst du nur ein, wo sie liegen.
2. Claude Desktop (Cowork) oder Claude Code installieren und `C:\Superhirn` als Arbeitsordner öffnen. Zusätzlich die echten Datenordner freigeben.
3. Skills installieren: Die vier Ordner unter `skills/` nach `%USERPROFILE%\.claude\skills\` kopieren. In der Claude-App gehen sie auch per Upload unter Einstellungen → Skills.
4. Gmail-Connector prüfen. Er ist in deinem Konto schon verbunden.
5. Die Lücken in den drei `CLAUDE.md` füllen. Alles in `[eckigen Klammern]` ist Platzhalter. Je genauer das ist, desto weniger musst du später korrigieren.
6. Beobachter starten (siehe unten).

## Beobachter

`protokoll/beobachter.ps1` merkt sich nur Dateinamen, Ordner und Uhrzeit. Kein Inhalt, keine Screenshots, keine Tastatureingaben.

Testweise starten:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Superhirn\protokoll\beobachter.ps1
```

Dauerhaft: In der Aufgabenplanung eine Aufgabe „Bei Anmeldung“ anlegen, die denselben Befehl mit `-WindowStyle Hidden` ausführt.

Welche Ordner beobachtet werden, steht oben im Skript. Standard sind Downloads, Dokumente und Desktop.

## Routinen

In Cowork unter „Geplante Aufgaben“ anlegen, oder in Claude Code mit `/schedule`:

| Wann | Was |
|---|---|
| Werktags 7:45 | `/mail-entwurf` für alle ungelesenen Mails seit gestern, nur Entwürfe |
| Werktags 17:10 | `/ablage-belege` für Downloads und Scan-Ordner, nur Vorschlagsliste |
| Freitags 15:50 | `/wochen-rueckblick` |

## Die ersten zwei Wochen

Woche 1 läuft nur der Beobachter und du nutzt die Skills von Hand. Jede Korrektur, die du zweimal machst, gehört als Regel in die passende `CLAUDE.md`.

Ab Woche 2 laufen die Routinen. Erst wenn die Entwürfe eine Woche lang ohne größere Änderungen durchgehen, lohnt es sich, über mehr Selbstständigkeit nachzudenken.
