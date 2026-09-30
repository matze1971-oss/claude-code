# Superhirn-Beobachter ARBEIT
# Schreibt mit, wann in den Arbeitsordnern Dateien angelegt, geändert, umbenannt oder gelöscht werden.
# Nur Pfad, Ereignis und Uhrzeit. Kein Dateiinhalt, keine Screenshots, keine Tastatur.
#
# Test:      powershell -ExecutionPolicy Bypass -File C:\Superhirn\arbeit\protokoll\beobachter.ps1
# Dauerhaft: Aufgabenplanung → Aufgabe "Bei Anmeldung" → gleicher Befehl mit -WindowStyle Hidden

# Nur berufliche Ordner eintragen. Downloads gehören ins Privathirn,
# außer du hast einen eigenen Download-Ordner für die Arbeit.
$Ordner = @(
    "D:\Arbeit"                 # [anpassen]
    # "D:\Arbeit\Belege-Eingang"
)

. (Join-Path $PSScriptRoot '..\..\beobachter-kern.ps1')
Start-Beobachter -Ordner $Ordner -Log (Join-Path $PSScriptRoot 'aktivitaet.csv')
