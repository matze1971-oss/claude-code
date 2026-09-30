---
name: arbeit-angebote-nachfassen
description: Findet per Mail verschickte Angebote im Gesendet-Ordner, prüft, ob der Kunde geantwortet hat, und legt nach der eingestellten Frist eine Nachfass-Mail als Entwurf an. Führt die Liste angebote.csv. Nutzen bei "Angebote nachfassen", "offene Angebote", "wer hat nicht geantwortet" im Arbeitshirn oder per Routine.
---

# Angebote nachfassen

Nur das Werkzeug `mail-arbeit` verwenden.

## Einstellungen

Stehen in `CLAUDE.md` unter „Angebote“: Frist bis zum ersten Nachfassen, Frist bis zum zweiten, Stichwörter.

## Ablauf

1. `angebote.csv` im Superhirn-Ordner Arbeit lesen. Spalten:
   `gesendet_am;empfaenger;kunde;betreff;uid_gesendet;status;nachgefasst_am;notiz`
   Fehlt die Datei, neu anlegen.
2. Im Gesendet-Ordner nach neuen Angeboten suchen: `mails_suchen(ordner="gesendet", seit_tagen=60, betreff=...)` für jedes Stichwort. Zusätzlich `volltext="Angebot"`, weil Angebote oft im Mailtext stehen und nicht im Betreff. Bei Zweifeln die Mail mit `mail_lesen` öffnen. Ein Angebot ist es, wenn Preis, Leistung und Aufforderung zur Rückmeldung drinstehen.
3. Neue Angebote mit Status `offen` in die Liste aufnehmen.
4. Für jedes offene Angebot im Posteingang nach einer Antwort suchen: `mails_suchen(von=<Empfängeradresse>, seit_tagen=<Tage seit Versand>)`. Gibt es eine, Status auf `antwort` setzen und in der Notiz kurz festhalten, was drinsteht (Zusage, Rückfrage, Absage).
5. Ist die Frist ohne Antwort abgelaufen, eine Nachfass-Mail als Entwurf anlegen: `entwurf_anlegen(antwort_auf_uid=<uid_gesendet>, antwort_ordner="gesendet", text=...)`. Status auf `nachgefasst`, Datum eintragen. Nach dem zweiten Nachfassen ohne Antwort Status `ruhend`, kein dritter Entwurf.
6. Nachfass-Text: zwei bis vier Sätze, Humanizer-Regeln aus `CLAUDE.md`, Ansprache aus der Kundentabelle. Keine Rabatte, keine neuen Termine, keine Zusagen erfinden. Beispiel für den Ton:

   > Hallo Herr Maier, ich wollte kurz nachhören, ob Sie sich das Angebot vom 12.09. schon ansehen konnten. Wenn noch etwas unklar ist, rufen Sie mich gern an.

## Ausgabe

```
Neu erkannt: 2
Antwort da: Kunde A (Zusage), Kunde C (Rückfrage zum Liefertermin)
Nachfass-Entwurf angelegt: Kunde B (Angebot vom 12.09., 14 Tage ohne Antwort)
Ruhend: 1
```

`angebote.csv` darf dieser Skill selbst schreiben. Sie ist die Merkliste des Superhirns, keine Kundendatei.
