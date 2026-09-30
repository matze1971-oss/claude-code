# Superhirn-Beobachter PRIVAT
# Schreibt mit, wann in den Privatordnern Dateien angelegt, geändert, umbenannt oder gelöscht werden.
# Nur Pfad, Ereignis und Uhrzeit. Kein Dateiinhalt, keine Screenshots, keine Tastatur.
#
# Test:      powershell -ExecutionPolicy Bypass -File C:\Superhirn\privat\protokoll\beobachter.ps1
# Dauerhaft: Aufgabenplanung → Aufgabe "Bei Anmeldung" → gleicher Befehl mit -WindowStyle Hidden

$Ordner = @(
    "$env:USERPROFILE\Downloads",
    "$env:USERPROFILE\Documents",
    "D:\Privat"                 # [anpassen]
    # "D:\Scans"
)

. (Join-Path $PSScriptRoot '..\..\beobachter-kern.ps1')
Start-Beobachter -Ordner $Ordner -Log (Join-Path $PSScriptRoot 'aktivitaet.csv')
