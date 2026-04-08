<#
.SYNOPSIS
    Find wiki pages not updated within N days.
.PARAMETER Days
    Number of days to consider a page stale. Default: 30.
.PARAMETER WikiPath
    Path to the wiki directory.
#>
param(
    [int]$Days = 30,
    [string]$WikiPath = ""
)

if (-not $WikiPath) {
    $WikiPath = Join-Path (Split-Path $PSScriptRoot -Parent) "wiki"
}

$cutoff = (Get-Date).AddDays(-$Days).ToString("yyyy-MM-dd")
$stalePages = @()

Get-ChildItem -Path $WikiPath -Recurse -Filter "*.md" | Where-Object {
    $_.DirectoryName -notlike "*_indexes*" -and $_.DirectoryName -notlike "*log*"
} | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return }

    $updated = ""
    if ($content -match 'updated:\s*(\d{4}-\d{2}-\d{2})') {
        $updated = $Matches[1]
    }

    if ($updated -and $updated -lt $cutoff) {
        $relPath = $_.FullName.Replace((Get-Item $WikiPath).FullName + "\", "").Replace("\", "/")
        $stalePages += [PSCustomObject]@{
            Path = $relPath
            LastUpdated = $updated
            DaysStale = ((Get-Date) - [DateTime]::Parse($updated)).Days
        }
    }
}

if ($stalePages.Count -eq 0) {
    Write-Host "No stale pages found (threshold: $Days days)."
} else {
    Write-Host "Found $($stalePages.Count) stale page(s) (not updated in $Days+ days):`n"
    $stalePages | Sort-Object DaysStale -Descending | ForEach-Object {
        Write-Host "  [$($_.DaysStale)d] $($_.Path) (last: $($_.LastUpdated))"
    }
}
