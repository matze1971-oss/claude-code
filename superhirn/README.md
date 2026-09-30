# Superhirn

Zwei getrennte Hirne für Matthias: eins für die Arbeit, eins für Privat. Sie teilen sich nichts. Jedes hat sein eigenes Gedächtnis, seine eigenen Skills, sein eigenes Mailkonto und sein eigenes Protokoll.

Grundregel in beiden: Das Superhirn bereitet vor, du entscheidest. Es schreibt Entwürfe und schlägt Ablageorte vor. Senden, verschieben und löschen passiert erst nach deiner Freigabe.

## Aufbau

```
Superhirn/
  arbeit/                     Hirn Arbeit, eigenständig
    CLAUDE.md                 Gedächtnis: Rolle, Kunden, Ablageplan, Schreibstil, Rechte
    .claude/skills/
      mail-entwurf/
      ablage-belege/
      dokument-vorlage/
      wochen-rueckblick/
    protokoll/
      beobachter.ps1          beobachtet nur Arbeitsordner
  privat/                     Hirn Privat, eigenständig
    CLAUDE.md
    .claude/skills/
      mail-entwurf/
      ablage-belege/          mit Steuer-Liste
      wochen-rueckblick/
    protokoll/
      beobachter.ps1          beobachtet nur Privatordner
  beobachter-kern.ps1         reine Logik für beide Beobachter, keine Daten
```

Jeder Beobachter schreibt in sein eigenes `protokoll/aktivitaet.csv`. Die Logs landen nie am selben Ort.

Die Skills liegen bewusst im jeweiligen Hirn unter `.claude/skills/` und nicht global. So kennt das Arbeitshirn die privaten Skills gar nicht, und umgekehrt.

## Warum getrennt

Ein gemeinsames Gedächtnis heißt, dass beim Mailschreiben für einen Kunden auch deine Versicherungsunterlagen im Kontext liegen können. Getrennt kann das technisch nicht passieren, weil jedes Hirn nur seinen eigenen Ordner sieht.

Der Preis: Den Schreibstil (Humanizer) gibt es zweimal. Wenn du ihn änderst, in beiden `CLAUDE.md` ändern.

## Einrichten

1. `superhirn` nach `C:\Superhirn` kopieren. Deine echten Datenordner bleiben, wo sie sind.
2. **Claude Code:** Je Hirn ein eigenes Fenster, gestartet im jeweiligen Ordner (`cd C:\Superhirn\arbeit` → `claude`). Die Skills unter `.claude/skills/` werden dann automatisch geladen. Den echten Datenordner mit `/add-dir` dazunehmen.
   **Cowork / Claude Desktop:** Zwei Projekte anlegen, „Arbeit“ und „Privat“. Den Inhalt der jeweiligen `CLAUDE.md` als Projekt-Anweisung eintragen, nur den passenden Ordner freigeben. Skills werden dort kontoweit hochgeladen (Einstellungen → Skills). Deshalb heißen sie unterschiedlich: `arbeit-mail-entwurf`, `privat-mail-entwurf` usw.
3. Mail: Das Arbeitshirn bekommt nur das Arbeitskonto, das Privathirn nur das private. Welches Konto wohin gehört, steht oben in der jeweiligen `CLAUDE.md`.
4. Platzhalter in `[eckigen Klammern]` füllen.
5. Beide Beobachter starten, jeder mit seinen Ordnern (Anleitung oben im Skript).

## Routinen

Zeitpläne und fertige Prompts zum Reinkopieren stehen in `routinen.md`. Die Belege- und Rückblick-Routinen laufen sofort, die Mail-Routinen erst, wenn der Mailzugang geklärt ist.

## Die ersten zwei Wochen

Woche 1 laufen nur die Beobachter, die Skills nutzt du von Hand. Jede Korrektur, die du zweimal machst, wird eine Regel in der passenden `CLAUDE.md`.

Ab Woche 2 laufen die Routinen. Mehr Selbstständigkeit erst, wenn die Entwürfe eine Woche lang fast unverändert durchgehen.
