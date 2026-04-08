<#
.SYNOPSIS
    Full-text search across all wiki pages with optional filtering by type and tags.
.PARAMETER Query
    The search term (case-insensitive substring match).
.PARAMETER Type
    Filter by page type (entity, concept, source, synthesis). Optional.
.PARAMETER Tags
    Filter by tag (comma-separated). Optional. Matches any tag.
.PARAMETER WikiPath
    Path to the wiki directory. Defaults to ./wiki relative to script location.
.PARAMETER MaxResults
    Maximum number of results to return. Default 50.
#>
param(
    [Parameter(Mandatory=$true)]
    [string]$Query,

    [string]$Type = "",

    [string]$Tags = "",

    [string]$WikiPath = "",

    [int]$MaxResults = 50
)

if (-not $WikiPath) {
    $WikiPath = Join-Path (Split-Path $PSScriptRoot -Parent) "wiki"
}

$results = @()
$tagList = if ($Tags) { $Tags -split ',' | ForEach-Object { $_.Trim().ToLower() } } else { @() }

Get-ChildItem -Path $WikiPath -Recurse -Filter "*.md" | Where-Object {
    $_.DirectoryName -notlike "*_indexes*" -and $_.DirectoryName -notlike "*log*"
} | ForEach-Object {
    $file = $_
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return }

    # Parse frontmatter
    $frontmatter = @{}
    if ($content -match "(?s)^---\r?\n(.+?)\r?\n---") {
        $fmText = $Matches[1]
        foreach ($line in ($fmText -split '\r?\n')) {
            if ($line -match '^(\w+):\s*(.+)$') {
                $key = $Matches[1].Trim()
                $val = $Matches[2].Trim().Trim('"').Trim("'")
                $frontmatter[$key] = $val
            }
        }
    }

    # Type filter
    if ($Type -and $frontmatter['type'] -and $frontmatter['type'] -ne $Type) { return }

    # Tag filter
    if ($tagList.Count -gt 0) {
        $pageTags = @()
        if ($frontmatter['tags']) {
            $pageTags = ($frontmatter['tags'] -replace '[\[\]]','') -split ',' | ForEach-Object { $_.Trim().ToLower() }
        }
        $matched = $false
        foreach ($t in $tagList) {
            if ($pageTags -contains $t) { $matched = $true; break }
        }
        if (-not $matched) { return }
    }

    # Content search
    if ($content -match [regex]::Escape($Query)) {
        $relativePath = $file.FullName.Replace((Get-Item $WikiPath).FullName, "wiki").Replace("\", "/")
        $title = if ($frontmatter['title']) { $frontmatter['title'] } else { $file.BaseName }
        $pageType = if ($frontmatter['type']) { $frontmatter['type'] } else { "unknown" }

        # Find matching lines for context
        $lines = $content -split '\r?\n'
        $matchLines = @()
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match [regex]::Escape($Query)) {
                $matchLines += "  L$($i+1): $($lines[$i].Trim().Substring(0, [Math]::Min(120, $lines[$i].Trim().Length)))"
                if ($matchLines.Count -ge 3) { break }
            }
        }

        $results += [PSCustomObject]@{
            Title   = $title
            Type    = $pageType
            Path    = $relativePath
            Matches = ($matchLines -join "`n")
        }
    }
}

if ($results.Count -eq 0) {
    Write-Host "No results found for '$Query'"
} else {
    $shown = [Math]::Min($results.Count, $MaxResults)
    Write-Host "Found $($results.Count) result(s) for '$Query' (showing $shown):`n"
    $results | Select-Object -First $MaxResults | ForEach-Object {
        Write-Host "[$($_.Type)] $($_.Title)"
        Write-Host "  Path: $($_.Path)"
        if ($_.Matches) { Write-Host $_.Matches }
        Write-Host ""
    }
}
