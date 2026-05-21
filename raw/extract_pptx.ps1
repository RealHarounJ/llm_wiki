Add-Type -AssemblyName System.IO.Compression.FileSystem
$pptxPath = "c:\Users\jaafa\Downloads\llm_wiki-main\raw\group 11.pptx"
$outputPath = "c:\Users\jaafa\Downloads\llm_wiki-main\raw\group_11_extracted.txt"

$zip = [System.IO.Compression.ZipFile]::OpenRead($pptxPath)
$slides = $zip.Entries | Where-Object { $_.FullName -match '^ppt/slides/slide\d+\.xml$' } | Sort-Object { 
    $num = $_.FullName -replace '\D'
    [int]$num 
}

$allText = ""
foreach ($slide in $slides) {
    $stream = $slide.Open()
    $reader = New-Object System.IO.StreamReader($stream)
    $xmlText = $reader.ReadToEnd()
    $reader.Close()
    $stream.Close()
    
    $matches = [regex]::Matches($xmlText, '<a:t[^>]*>(.*?)</a:t>')
    $slideText = New-Object System.Collections.Generic.List[string]
    foreach ($m in $matches) {
        $val = $m.Groups[1].Value
        # Decode HTML entities if any
        $val = [System.Web.HttpUtility]::HtmlDecode($val)
        if ($val.Trim()) {
            $slideText.Add($val.Trim())
        }
    }
    
    $slideNum = $slide.FullName -replace '\D'
    $allText += "=== SLIDE $slideNum ===`r`n" + ($slideText -join "`r`n") + "`r`n`r`n"
}
$zip.Dispose()
[System.IO.File]::WriteAllText($outputPath, $allText)
Write-Output "Extracted successfully to group_11_extracted.txt!"
