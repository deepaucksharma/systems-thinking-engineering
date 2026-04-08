<#
.SYNOPSIS
    Display wiki statistics: page counts, tag distribution, link density.
.PARAMETER WikiPath
    Path to the wiki directory.
#>
param(
    [string]$WikiPath = ""
)

if (-not $WikiPath) {
    $WikiPath = Join-Path (Split-Path $PSScriptRoot -Parent) "wiki"
}

$allPages = Get-ChildItem -Path $WikiPath -Recurse -Filter "*.md" | Where-Object {
    $_.DirectoryName -notlike "*_indexes*" -and $_.DirectoryName -notlike "*log*"
}

$typeCounts = @{}
$tagCounts = @{}
$statusCounts = @{}
$totalLinks = 0

foreach ($page in $allPages) {
    $content = Get-Content $page.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    if ($content -match "(?s)^---\r?\n(.+?)\r?\n---") {
        $fmText = $Matches[1]
        $fields = @{}
        foreach ($line in ($fmText -split '\r?\n')) {
            if ($line -match '^(\w+):\s*(.+)$') {
                $fields[$Matches[1].Trim()] = $Matches[2].Trim()
            }
        }

        $t = if ($fields['type']) { $fields['type'].Trim('"').Trim("'") } else { "unknown" }
        if (-not $typeCounts.ContainsKey($t)) { $typeCounts[$t] = 0 }
        $typeCounts[$t] += 1

        if ($fields['tags']) {
            $tags = ($fields['tags'] -replace '[\[\]]','') -split ',' | ForEach-Object { $_.Trim().ToLower() }
            foreach ($tag in $tags) {
                if ($tag) {
                    if (-not $tagCounts.ContainsKey($tag)) { $tagCounts[$tag] = 0 }
                    $tagCounts[$tag] += 1
                }
            }
        }

        $s = if ($fields['status']) { $fields['status'].Trim('"').Trim("'") } else { "unknown" }
        if (-not $statusCounts.ContainsKey($s)) { $statusCounts[$s] = 0 }
        $statusCounts[$s] += 1
    }

    $linkMatches = [regex]::Matches($content, '\[.+?\]\([^)]+\.md\)')
    $totalLinks += $linkMatches.Count
}

Write-Host "=== Wiki Statistics ==="
Write-Host ""
Write-Host "Total pages: $($allPages.Count)"
Write-Host ""

Write-Host "By type:"
$typeCounts.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "  $($_.Name): $($_.Value)"
}
Write-Host ""

Write-Host "By status:"
$statusCounts.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host "  $($_.Name): $($_.Value)"
}
Write-Host ""

Write-Host "Total outbound links: $totalLinks"
if ($allPages.Count -gt 0) {
    Write-Host "Average links per page: $([Math]::Round($totalLinks / $allPages.Count, 1))"
}
Write-Host ""

Write-Host "Top tags:"
$tagCounts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 20 | ForEach-Object {
    Write-Host "  $($_.Name): $($_.Value)"
}
