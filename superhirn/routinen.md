# Routinen für Cowork

Zum Abtippen bzw. Reinkopieren in Cowork. Jede Routine wird im passenden Projekt angelegt, damit sie nur dessen Ordner und Anweisungen sieht.

## So legst du eine Routine an

1. Claude Desktop öffnen, links auf **Cowork**, dann das Projekt wählen (Arbeit oder Privat).
2. Links auf **Geplant** (Scheduled) → **Neue Aufgabe**. Alternativ in einer laufenden Aufgabe `/schedule` eintippen.
3. Name, Zeitplan und Prompt aus der Tabelle unten eintragen.
4. Bei den Ordnerrechten nur die Ordner freigeben, die bei der Routine stehen.

Wichtig: Geplante Aufgaben laufen nur, wenn der PC an ist und Claude Desktop läuft. Ist der PC zur geplanten Zeit aus, wird die Aufgabe beim nächsten Start nachgeholt oder fällt aus, je nach Version. Das nach der ersten Woche prüfen.

Jede Routine startet ohne Erinnerung an den letzten Lauf. Deshalb stehen in den Prompts alle Anweisungen komplett.

## Laufen sofort

### Arbeit: Belege am Abend

- Projekt: Arbeit
- Zeitplan: Montag bis Freitag, 17:10
- Ordner: Arbeitsordner, Beleg-Eingang Arbeit, `C:\Superhirn\arbeit`

```
Führe den Skill arbeit-ablage-belege aus. Quelle ist nur der Beleg-Eingang Arbeit
aus den Projekt-Anweisungen. Verschiebe und benenne nichts um. Erstelle nur die
Vorschlagstabelle und speichere sie als _entwuerfe/ablage-vorschlag_<Datum>.md
im Arbeitsordner. Gibt es keine neuen Dateien, schreib nur "Nichts Neues" in die
Zusammenfassung.
```

### Arbeit: Wochenrückblick

- Projekt: Arbeit
- Zeitplan: Freitag, 15:50
- Ordner: Arbeitsordner, `C:\Superhirn\arbeit`

```
Führe den Skill arbeit-wochen-rueckblick für die letzten 7 Tage aus. Quellen:
C:\Superhirn\arbeit\protokoll\aktivitaet.csv und ablage.log. Mails nur, wenn ein
Mailzugang verbunden ist. Speichere das Ergebnis als
_entwuerfe/wochenrueckblick_<Datum>.md. Höchstens fünf Vorschläge, keine erfundenen.
```

### Privat: Belege und Scans

- Projekt: Privat
- Zeitplan: Samstag, 9:50
- Ordner: Privatordner, Downloads, Scan-Eingang, `C:\Superhirn\privat`

```
Führe den Skill privat-ablage-belege aus. Quellen: Downloads und Scan-Eingang aus
den Projekt-Anweisungen. Verschiebe und benenne nichts um, schreib nichts in die
Steuer-Liste. Erstelle nur die Vorschlagstabelle mit Steuer-Spalte und speichere
sie als _entwuerfe/ablage-vorschlag_<Datum>.md im Privatordner.
```

### Privat: Wochenrückblick mit Fristen

- Projekt: Privat
- Zeitplan: Samstag, 10:10
- Ordner: Privatordner, `C:\Superhirn\privat`

```
Führe den Skill privat-wochen-rueckblick aus. Zuerst alle Fristen und Zahlungen
der nächsten 30 Tage aus der Vertragstabelle in den Projekt-Anweisungen. Danach
Muster aus C:\Superhirn\privat\protokoll\aktivitaet.csv. Speichere das Ergebnis als
_entwuerfe/wochenrueckblick_<Datum>.md.
```

## Nach Einrichtung des Mail-Bausteins

Erst anlegen, wenn `mail-arbeit` bzw. `mail-privat` unter Einstellungen → Entwickler als „running“ erscheinen (siehe `mail-baustein/README.md`).

### Arbeit: Postfach am Morgen

- Projekt: Arbeit
- Zeitplan: Montag bis Freitag, 7:45

```
Führe den Skill arbeit-mail-entwurf mit dem Werkzeug mail-arbeit aus: ungelesene Mails
seit dem letzten Werktag.
Nur Entwürfe anlegen, nichts senden, nichts löschen, nichts als gelesen markieren.
Übersicht als _entwuerfe/postfach_<Datum>.md speichern.
```

### Privat: Postfach am Abend (vorerst nicht anlegen)

Das Privatkonto ist nicht angebunden. Bei ca. 2 Mails pro Woche lohnt sich die Routine nicht.

- Projekt: Privat
- Zeitplan: täglich, 19:10

```
Führe den Skill privat-mail-entwurf mit dem Werkzeug mail-privat aus: ungelesene
Mails seit gestern.
Preiserhöhungen und Fristen oben melden. Nur Entwürfe, nichts senden oder löschen.
Übersicht als _entwuerfe/postfach_<Datum>.md speichern.
```

### Arbeit: Angebote nachfassen

- Projekt: Arbeit
- Zeitplan: Montag bis Freitag, 8:10
- Ordner: `C:\Superhirn\arbeit`

```
Führe den Skill arbeit-angebote-nachfassen mit dem Werkzeug mail-arbeit aus.
Fristen und Stichwörter stehen in den Projekt-Anweisungen unter "Angebote".
Nur Entwürfe anlegen. angebote.csv aktualisieren. Übersicht als
_entwuerfe/angebote_<Datum>.md speichern.
```

## Ausbau (vorgemerkt)

- **Morgenbriefing Arbeit**, werktags 7:50: Termine des Tages, offene Entwürfe, fällige Nachfass-Mails. Offen ist, wo dein Kalender liegt. Bei einem IMAP-Konto in Outlook meist nur lokal auf dem PC.
