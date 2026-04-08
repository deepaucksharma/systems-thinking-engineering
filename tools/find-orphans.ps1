<#
.SYNOPSIS
    Find wiki pages with no inbound backlinks (orphan pages).
.PARAMETER WikiPath
    Path to the wiki directory. Defaults to ./wiki relative to script location.
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

# Build a map of all page filenames
$pageMap = @{}
foreach ($page in $allPages) {
    $relPath = $page.FullName.Replace((Get-Item $WikiPath).FullName + "\", "").Replace("\", "/")
    $pageMap[$relPath] = @{
        Title = $page.BaseName
        InboundCount = 0
        FullPath = $page.FullName
    }
}

# Scan all pages for outbound links and count inbound references
foreach ($page in $allPages) {
    $content = Get-Content $page.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    # Find all markdown links like [text](../path/file.md) or [text](path/file.md)
    $linkPattern = '\[.+?\]\(([^)]+\.md)\)'
    $matches = [regex]::Matches($content, $linkPattern)
    foreach ($m in $matches) {
        $linkTarget = $m.Groups[1].Value
        # Normalize: remove ../ prefixes and normalize slashes
        $normalized = $linkTarget -replace '\.\./', '' -replace '\\', '/'
        if ($pageMap.ContainsKey($normalized)) {
            $pageMap[$normalized].InboundCount++
        }
    }
}

# Report orphans
$orphans = $pageMap.GetEnumerator() | Where-Object { $_.Value.InboundCount -eq 0 } | Sort-Object { $_.Key }

if ($orphans.Count -eq 0) {
    Write-Host "No orphan pages found. All pages have at least one inbound link."
} else {
    Write-Host "Found $($orphans.Count) orphan page(s) with no inbound links:`n"
    foreach ($orphan in $orphans) {
        Write-Host "  - $($orphan.Key)"
    }
}
