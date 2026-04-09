<#
.SYNOPSIS
    Report broken .md links, empty markdown links, and basic frontmatter path issues in the wiki.
.DESCRIPTION
    Resolves relative [text](path.md) targets from each file's directory. Optionally checks
    frontmatter list entries that look like wiki/... paths against the repo root.
.PARAMETER WikiPath
    Path to wiki directory (default: ../wiki from script location).
.PARAMETER RepoRoot
    Repository root for resolving wiki/... paths in YAML (default: parent of tools/).
#>
param(
    [string]$WikiPath = "",
    [string]$RepoRoot = ""
)

if (-not $WikiPath) {
    $WikiPath = Join-Path (Split-Path $PSScriptRoot -Parent) "wiki"
}
if (-not $RepoRoot) {
    $RepoRoot = Split-Path $PSScriptRoot -Parent
}

$wikiRoot = (Get-Item $WikiPath).FullName

function Resolve-FromFile {
    param([string]$FromFile, [string]$Href)
    if ($Href -match '^(https?:|mailto:|#)') { return $null }
    if ($Href -notmatch '\.md([\#]|$)') { return $null }
    $pathOnly = ($Href -split '#')[0]
    if ([string]::IsNullOrWhiteSpace($pathOnly)) { return $null }
    $baseDir = [System.IO.Path]::GetDirectoryName($FromFile)
    try {
        $combined = [System.IO.Path]::GetFullPath((Join-Path $baseDir $pathOnly))
    } catch {
        return "invalid"
    }
    if (-not $combined.StartsWith($wikiRoot, [StringComparison]::OrdinalIgnoreCase)) {
        return "outside-wiki"
    }
    return $combined
}

function Resolve-WikiKey {
    param([string]$KeyPath)
    $norm = $KeyPath -replace '\\', '/' -replace '^wiki/', 'wiki\'
    $full = Join-Path $RepoRoot $norm
    try {
        return [System.IO.Path]::GetFullPath($full)
    } catch {
        return $null
    }
}

$allMd = Get-ChildItem -Path $WikiPath -Recurse -Filter "*.md"
$broken = [System.Collections.ArrayList]::new()
$emptyLinks = [System.Collections.ArrayList]::new()
$badFrontmatter = [System.Collections.ArrayList]::new()
$conflictingTags = [System.Collections.ArrayList]::new()

$yamlListPattern = '^\s*-\s*(wiki/[^\]\s`]+\.md)\s*$'
$inlineListPattern = '\[(wiki/[^\]]+\.md)\]'

foreach ($f in $allMd) {
    $raw = Get-Content $f.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $raw) { continue }

    foreach ($m in [regex]::Matches($raw, '\[[^\]]*\]\(\s*\)')) {
        [void]$emptyLinks.Add("${($f.FullName)}: $($m.Value)")
    }

    foreach ($m in [regex]::Matches($raw, '\[[^\]]*\]\(([^)]+)\)')) {
        $href = $m.Groups[1].Value.Trim()
        if ([string]::IsNullOrWhiteSpace($href)) { continue }
        $resolved = Resolve-FromFile -FromFile $f.FullName -Href $href
        if ($resolved -eq "invalid" -or $resolved -eq "outside-wiki") {
            [void]$broken.Add("$($f.FullName) -> $href ($resolved)")
            continue
        }
        if ($resolved -and -not (Test-Path -LiteralPath $resolved)) {
            [void]$broken.Add("$($f.FullName) -> $href")
        }
    }

    if ($raw -match '(?s)^---\r?\n(.+?)\r?\n---') {
        $fm = $Matches[1]
        foreach ($line in $fm -split '\r?\n') {
            if ($line -match $yamlListPattern) {
                $p = Resolve-WikiKey $Matches[1]
                if ($p -and -not (Test-Path -LiteralPath $p)) {
                    [void]$badFrontmatter.Add("$($f.Name) YAML: $($Matches[1]) -> missing")
                }
            }
        }
        foreach ($m in [regex]::Matches($fm, $inlineListPattern)) {
            $p = Resolve-WikiKey $m.Groups[1].Value
            if ($p -and -not (Test-Path -LiteralPath $p)) {
                [void]$badFrontmatter.Add("$($f.Name) YAML: $($m.Groups[1].Value) -> missing")
            }
        }
        if ($fm -match 'v2\.1-canonical' -and $fm -match 'v2-framework' -and $fm -match '^tags:') {
            [void]$conflictingTags.Add($f.FullName)
        }
    }
}

Write-Host "=== Empty markdown links: $($emptyLinks.Count) ==="
$emptyLinks | Sort-Object | ForEach-Object { Write-Host $_ }

Write-Host "`n=== Broken .md link targets: $($broken.Count) ==="
$broken | Sort-Object | ForEach-Object { Write-Host $_ }

Write-Host "`n=== Frontmatter wiki/*.md missing on disk: $($badFrontmatter.Count) ==="
$badFrontmatter | Sort-Object | ForEach-Object { Write-Host $_ }

Write-Host "`n=== Pages with both v2.1-canonical and v2-framework in frontmatter: $($conflictingTags.Count) ==="
$conflictingTags | Sort-Object | ForEach-Object { Write-Host- }

if ($broken.Count -gt 0 -or $emptyLinks.Count -gt 0 -or $badFrontmatter.Count -gt 0) {
    exit 1
}
exit 0
