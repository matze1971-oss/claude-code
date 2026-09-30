# Superhirn-Beobachter
# Schreibt mit, wann in welchen Ordnern Dateien angelegt, geändert, umbenannt oder gelöscht werden.
# Nur Pfad, Ereignis und Uhrzeit. Kein Dateiinhalt, keine Screenshots, keine Tastatur.

$Ordner = @(
    "$env:USERPROFILE\Downloads",
    "$env:USERPROFILE\Documents",
    "$env:USERPROFILE\Desktop"
    # "D:\Arbeit",
    # "D:\Privat"
)

# Temporäre und Systemdateien ignorieren
$Ignorieren = '(\\~\$|\.tmp$|\.crdownload$|\.part$|\\\.git\\|\\AppData\\|desktop\.ini$|Thumbs\.db$)'

$Log = Join-Path $PSScriptRoot 'aktivitaet.csv'
if (-not (Test-Path $Log)) {
    'Zeit;Ereignis;Ordner;Datei;AlterName' | Out-File -FilePath $Log -Encoding utf8
}

$Aktion = {
    $pfad = $Event.SourceEventArgs.FullPath
    if ($pfad -match $Event.MessageData.Ignorieren) { return }
    $alt = ''
    if ($Event.SourceEventArgs -is [System.IO.RenamedEventArgs]) {
        $alt = Split-Path $Event.SourceEventArgs.OldFullPath -Leaf
    }
    $zeile = '{0};{1};{2};{3};{4}' -f (Get-Date -Format 's'),
        $Event.SourceEventArgs.ChangeType,
        (Split-Path $pfad -Parent),
        (Split-Path $pfad -Leaf),
        $alt
    Add-Content -Path $Event.MessageData.Log -Value $zeile -Encoding utf8
}

$Daten = @{ Log = $Log; Ignorieren = $Ignorieren }

foreach ($o in $Ordner) {
    if (-not (Test-Path $o)) { Write-Warning "Ordner fehlt: $o"; continue }
    $w = New-Object System.IO.FileSystemWatcher $o
    $w.IncludeSubdirectories = $true
    $w.NotifyFilter = [System.IO.NotifyFilters]'FileName, LastWrite'
    $w.EnableRaisingEvents = $true
    foreach ($e in 'Created', 'Changed', 'Renamed', 'Deleted') {
        Register-ObjectEvent $w $e -Action $Aktion -MessageData $Daten | Out-Null
    }
}

Write-Host "Beobachter läuft. Protokoll: $Log  (Beenden mit Strg+C)"
while ($true) { Start-Sleep -Seconds 60 }
