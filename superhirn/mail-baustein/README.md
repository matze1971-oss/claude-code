# Mail-Baustein

Verbindet Cowork mit deinem Geschäftspostfach bei mail.de (`mail-arbeit`). Ein zweites Konto für Privat lässt sich später genauso ergänzen: gleicher Block mit `SUPERHIRN_KONTO=privat` unter dem Namen `mail-privat`.

Der Baustein kann:

- Ordner auflisten
- Mails suchen und lesen, ohne sie als gelesen zu markieren
- Antworten und neue Mails als **Entwurf** in den Entwürfe-Ordner legen
- Anhänge in einen festen Eingangsordner speichern

Senden, löschen, verschieben oder markieren kann er nicht, weil es diese Funktionen im Code schlicht nicht gibt. Selbst ein Fehler in einem Skill kann also keine Mail rausschicken. Die Entwürfe tauchen in Outlook unter dem Postfach im Ordner „Entwürfe“ auf. Dort prüfst du und klickst auf Senden.

## Einrichten unter Windows (ca. 20 Minuten)

1. **Python installieren**: python.org → Download für Windows, Version 3.11 oder neuer. Beim Installieren den Haken bei „Add python.exe to PATH“ setzen.
2. **IMAP beim Anbieter freischalten**: Bei vielen Anbietern (web.de, GMX, T-Online) muss IMAP erst in den Einstellungen des Webmailers aktiviert werden. Manche verlangen ein eigenes App-Passwort. Die Server-Adresse steht in der Hilfe des Anbieters oder in Outlook unter Datei → Kontoeinstellungen → Konto ändern.
3. **Baustein installieren**, in der Eingabeaufforderung:
   ```
   cd C:\Superhirn\mail-baustein
   py -m venv .venv
   .venv\Scripts\pip install -r requirements.txt
   ```
4. **Passwörter sicher ablegen**, je Konto einmal:
   ```
   .venv\Scripts\python passwort_speichern.py matthias@firma.de
   .venv\Scripts\python passwort_speichern.py privat@anbieter.de
   ```
   Die Passwörter liegen dann in der Windows-Anmeldeinformationsverwaltung, nicht in einer Datei.
5. **In Claude Desktop eintragen**: Einstellungen → Entwickler → Konfiguration bearbeiten. Das öffnet `%APPDATA%\Claude\claude_desktop_config.json`. Den Inhalt von `claude_desktop_config.beispiel.json` übernehmen und Server, Adressen und Ordner anpassen. Steht in der Datei schon etwas, nur den Block `mcpServers` ergänzen.
6. Claude Desktop ganz beenden (auch im Tray) und neu starten. Unter Einstellungen → Entwickler sollten `mail-arbeit` und `mail-privat` als „running“ erscheinen.
7. **Test** im Projekt Arbeit: „Nutze mail-arbeit: Zeig mir die Ordner und die letzten 5 Mails im Posteingang.“ Danach im Webmailer nachsehen, ob die Mails noch ungelesen sind.

## Optionale Einstellungen

| Variable | Wofür |
|---|---|
| `IMAP_PORT` | Standard 993 |
| `IMAP_SICHERHEIT` | `ssl` (Standard) oder `starttls` für Port 143 |
| `IMAP_ABSENDER` | Absender im Entwurf, z. B. `Matthias Nachname <matthias@firma.de>` |
| `IMAP_ORDNER_GESENDET` | falls der Gesendet-Ordner nicht automatisch gefunden wird |
| `IMAP_ORDNER_ENTWUERFE` | dasselbe für Entwürfe |

## Grenze der Trennung

Solange nur `mail-arbeit` eingetragen ist, gibt es dieses Problem nicht: Das Privathirn hat schlicht kein Postfach.

Sobald später auch `mail-privat` dazukommt:

Beide Instanzen sind in Claude Desktop für alle Projekte sichtbar. Dass das Arbeitshirn nur `mail-arbeit` benutzt, steht in dessen Anweisungen, technisch erzwungen ist es nicht. Wer das hart trennen will, braucht zwei Windows-Benutzerkonten mit je einer Claude-Desktop-Installation.

## Ordner bei mail.de mit Outlook

Outlook zeigt den Server-Ordner `Sent` als „Sent Items“ an. Der Baustein findet ihn über die offizielle Kennung von selbst. Die leeren Ordner `Gesendete Elemente`, `Sent Messages` und `Entwürfe` sind Altlasten und werden nicht benutzt.

## Getestet

Gegen einen lokalen IMAP-Testserver: Suchen mit Umlauten, Lesen ohne Gelesen-Markierung, Antwortentwurf mit Verlauf, Anhänge mit Sonderzeichen im Namen.

Auf dem echten PC (Windows, Python 3.14, mail.de): Login, Ordnerliste, Suche im Gesendet-Ordner und ein Testentwurf, der in Outlook unter Entwürfe erscheint.

## Claude Desktop aus dem Microsoft Store

Die Store-Version hatte früher einen eigenen Datenordner unter `%LOCALAPPDATA%\Packages\Claude_…\LocalCache\Roaming\Claude`. Neuere Versionen nutzen wieder `%APPDATA%\Claude`. Maßgeblich ist der Pfad, der unter Einstellungen → Entwickler bei den laufenden Servern steht.
