# Gemeinsamer Code für beide Beobachter. Enthält keine Daten, nur die Logik.
# Wird von arbeit\protokoll\beobachter.ps1 und privat\protokoll\beobachter.ps1 geladen.

function Start-Beobachter {
    param(
        [string[]]$Ordner,
        [string]$Log
    )

    # Temporäre und Systemdateien ignorieren
    $ignorieren = '(\\~\$|\.tmp$|\.crdownload$|\.part$|\\\.git\\|\\AppData\\|desktop\.ini$|Thumbs\.db$)'

    if (-not (Test-Path $Log)) {
        'Zeit;Ereignis;Ordner;Datei;AlterName' | Out-File -FilePath $Log -Encoding utf8
    }

    $aktion = {
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

    $daten = @{ Log = $Log; Ignorieren = $ignorieren }

    foreach ($o in $Ordner) {
        if (-not (Test-Path $o)) { Write-Warning "Ordner fehlt: $o"; continue }
        $w = New-Object System.IO.FileSystemWatcher $o
        $w.IncludeSubdirectories = $true
        $w.NotifyFilter = [System.IO.NotifyFilters]'FileName, LastWrite'
        $w.EnableRaisingEvents = $true
        foreach ($e in 'Created', 'Changed', 'Renamed', 'Deleted') {
            Register-ObjectEvent $w $e -Action $aktion -MessageData $daten | Out-Null
        }
    }

    Write-Host "Beobachter läuft. Protokoll: $Log  (Beenden mit Strg+C)"
    while ($true) { Start-Sleep -Seconds 60 }
}
