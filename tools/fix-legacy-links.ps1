$files = Get-ChildItem -Path "wiki/concepts" -Filter "*.md"
$replacements = @{
    "../legacy/value-alignment.md" = "10-block-V.md"
    "../legacy/people-system.md" = "11-block-P.md"
    "../legacy/execution-system.md" = "12-block-E.md"
    "../legacy/org-alignment.md" = "13-block-A.md"
    "../legacy/learning-adaptation.md" = "14-block-L.md"
    "../legacy/master-equation.md" = "02-master-equation.md"
    "../legacy/clarity.md" = "12-block-E.md"
    "../legacy/focus.md" = "12-block-E.md"
    "../legacy/skill.md" = "12-block-E.md"
    "../legacy/coordination.md" = "12-block-E.md"
    "../legacy/quality.md" = "12-block-E.md"
    "../legacy/nyquist-constraint.md" = "06-time-constants.md"
    "../legacy/zero-override-rule.md" = "21-zero-override.md"
    "../legacy/metrics-framework.md" = "41-metrics-by-block.md"
    "../legacy/anti-patterns.md" = "51-anti-patterns.md"
    "../legacy/fix-order.md" = "20-diagnostic-sequence.md"
    "../legacy/feedback-speed.md" = "14-block-L.md"
}

foreach ($file in $files) {
    $content = Get-Content -Raw -Path $file.FullName
    $modified = $false
    
    foreach ($key in $replacements.Keys) {
        if ($content -match \[System.Text.RegularExpressions.Regex\]::Escape($key)) {
            $content = $content -replace \[System.Text.RegularExpressions.Regex\]::Escape($key), $replacements[$key]
            $modified = $true
        }
    }
    
    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Updated $($file.Name)"
    }
}
