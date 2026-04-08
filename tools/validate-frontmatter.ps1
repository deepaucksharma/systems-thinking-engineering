<#
.SYNOPSIS
    Validate YAML frontmatter compliance for all wiki pages.
.PARAMETER WikiPath
    Path to the wiki directory.
#>
param(
    [string]$WikiPath = ""
)

if (-not $WikiPath) {
    $WikiPath = Join-Path (Split-Path $PSScriptRoot -Parent) "wiki"
}

$requiredFields = @("title", "type", "tags", "sources", "created", "updated", "status")
$validTypes = @("entity", "concept", "source", "synthesis")
$validStatuses = @("active", "stub", "stale")
$issues = @()

Get-ChildItem -Path $WikiPath -Recurse -Filter "*.md" | Where-Object {
    $_.DirectoryName -notlike "*_indexes*" -and $_.DirectoryName -notlike "*log*"
} | ForEach-Object {
    $file = $_
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return }

    $relPath = $file.FullName.Replace((Get-Item $WikiPath).FullName + "\", "").Replace("\", "/")

    # Check for frontmatter existence
    if ($content -notmatch "(?s)^---\r?\n(.+?)\r?\n---") {
        $issues += "$relPath — MISSING FRONTMATTER"
        return
    }

    $fmText = $Matches[1]
    $fields = @{}
    foreach ($line in ($fmText -split '\r?\n')) {
        if ($line -match '^(\w+):\s*(.*)$') {
            $fields[$Matches[1].Trim()] = $Matches[2].Trim()
        }
    }

    foreach ($req in $requiredFields) {
        if (-not $fields.ContainsKey($req) -or [string]::IsNullOrWhiteSpace($fields[$req])) {
            $issues += "$relPath — MISSING FIELD: $req"
        }
    }

    if ($fields['type'] -and $validTypes -notcontains $fields['type'].Trim('"').Trim("'")) {
        $issues += "$relPath — INVALID TYPE: $($fields['type']) (expected: $($validTypes -join ', '))"
    }

    if ($fields['status'] -and $validStatuses -notcontains $fields['status'].Trim('"').Trim("'")) {
        $issues += "$relPath — INVALID STATUS: $($fields['status']) (expected: $($validStatuses -join ', '))"
    }
}

if ($issues.Count -eq 0) {
    Write-Host "All wiki pages pass frontmatter validation."
} else {
    Write-Host "Found $($issues.Count) frontmatter issue(s):`n"
    $issues | ForEach-Object { Write-Host "  $_" }
}
