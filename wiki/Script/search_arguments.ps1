$filePath = "c:\Users\jaafa\Downloads\llm_wiki-main\raw\Corporate finance.md"
$content = [System.IO.File]::ReadAllText($filePath)

# Let's search for "tax" AND "agency" AND "efficiency" in close proximity
# Proximity pattern: (tax|agency|efficiency) within 500 characters of each other
$pattern = "(?i)(?:tax|agency|efficiency).{0,500}(?:tax|agency|efficiency).{0,500}(?:tax|agency|efficiency)"
$matches = [regex]::Matches($content, $pattern)

Write-Host "Total content length: $($content.Length)"
Write-Host "Proximity matches found: $($matches.Count)"

$i = 0
foreach ($match in $matches) {
    $i++
    $start = [Math]::Max(0, $match.Index - 200)
    $len = [Math]::Min($content.Length - $start, $match.Length + 400)
    $snippet = $content.Substring($start, $len)
    
    Write-Host "`n--- Match $i at index $($match.Index) ---"
    Write-Host $snippet.Trim().Replace("`r`n", " ").Replace("`n", " ")
    
    if ($i -ge 20) {
        Write-Host "`nTruncating output..."
        break
    }
}
