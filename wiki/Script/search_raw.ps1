$filePath = "c:\Users\jaafa\Downloads\llm_wiki-main\raw\Corporate finance.md"
$content = [System.IO.File]::ReadAllText($filePath)

$pattern = "(?i).{0,150}(?:intermediar|mutual fund|pension fund|insurance comp|financial institution|financial market).{0,150}"
$matches = [regex]::Matches($content, $pattern)

Write-Output "Total length of file: $($content.Length)"
Write-Output "Matches found: $($matches.Count)"

$i = 0
foreach ($match in $matches) {
    $i++
    Write-Output "`n--- Match $i at index $($match.Index) ---"
    Write-Output $match.Value.Trim().Replace("`r`n", " ").Replace("`n", " ")
    if ($i -ge 40) {
        Write-Output "`nTruncating output..."
        break
    }
}
