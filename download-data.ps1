# Download creditcard.csv from Google Drive into ./data.
# FILE_ID is baked in; this script does not read .env.
# Windows counterpart of download-data (that script is macOS / Linux).
param(
    [switch]$Force,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ErrorActionPreference = "Stop"

$Root = (Resolve-Path $PSScriptRoot).Path
$FileId = "1TG96N6lxz9ikIl2I7Z9X9PrqGkkkP8CE"
$Csv = Join-Path $Root "data\creditcard.csv"
$Zip = Join-Path $Root "creditcard.csv.zip"

function Show-Usage {
    @"
Usage: .\download-data.ps1 [-Force]

  Download creditcard.csv.zip from Google Drive and unzip it to data\creditcard.csv.
  Skips the download when data\creditcard.csv is already present.

  -Force    Download and overwrite even if the CSV exists.
"@
}

if ($ExtraArgs -contains "-h" -or $ExtraArgs -contains "--help" -or $ExtraArgs -contains "-?") {
    Show-Usage
    exit 0
}
if ($ExtraArgs) {
    Show-Usage
    exit 1
}

if ((Test-Path $Csv) -and -not $Force) {
    Write-Host "already present: $Csv"
    exit 0
}

$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$confirmUri = "https://drive.google.com/uc?export=download&id=$FileId"
$html = Invoke-WebRequest -Uri $confirmUri -WebSession $session -UseBasicParsing
$uuid = $null
if ($html.Content -match 'name="uuid" value="([^"]+)"') {
    $uuid = $Matches[1]
}

try {
    if ($uuid) {
        $downloadUri = "https://drive.usercontent.google.com/download?id=$FileId&export=download&confirm=t&uuid=$uuid"
        Invoke-WebRequest -Uri $downloadUri -WebSession $session -OutFile $Zip -UseBasicParsing
    }
    else {
        Invoke-WebRequest -Uri "$confirmUri&confirm=t" -WebSession $session -OutFile $Zip -UseBasicParsing
    }

    $dataDir = Join-Path $Root "data"
    New-Item -ItemType Directory -Path $dataDir -Force | Out-Null
    Expand-Archive -Path $Zip -DestinationPath $dataDir -Force
}
finally {
    if (Test-Path $Zip) {
        Remove-Item -Force $Zip
    }
}

if (-not (Test-Path $Csv)) {
    Write-Error "zip did not contain creditcard.csv (is the Drive file shared with anyone with the link?)."
}

Write-Host "wrote $Csv"
