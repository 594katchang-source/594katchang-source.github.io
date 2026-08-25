param(
  [Parameter(Mandatory = $true)][string]$DocxPath,
  [Parameter(Mandatory = $true)][string]$OutputJson,
  [Parameter(Mandatory = $true)][string]$OutputHtml,
  [Parameter(Mandatory = $true)][string]$ManifestPath
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

$wNs = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
$ns = New-Object System.Xml.XmlNamespaceManager((New-Object System.Xml.NameTable))
$ns.AddNamespace('w', $wNs)

function Get-AttrValue([System.Xml.XmlNode]$Node, [string]$Name) {
  if ($null -eq $Node) { return '' }
  return $Node.GetAttribute($Name, $wNs)
}

function Get-SequenceText([System.Xml.XmlNode]$Node) {
  $parts = New-Object System.Collections.Generic.List[string]
  foreach ($child in $Node.SelectNodes('.//w:t | .//w:br | .//w:tab', $ns)) {
    if ($child.LocalName -eq 't') { [void]$parts.Add($child.InnerText) }
    elseif ($child.LocalName -eq 'tab') { [void]$parts.Add("`t") }
    else { [void]$parts.Add("`n") }
  }
  return ($parts -join '')
}

function Html([string]$Value) {
  return [System.Net.WebUtility]::HtmlEncode([string]$Value)
}

function Linkify([string]$Value) {
  $normalized = ([string]$Value).Replace("`r`n", "`n").Replace("`r", "`n")
  $tokens = @{}
  $tokenIndex = 0
  $normalized = [regex]::Replace($normalized, '\[(https?://[^\]\s]+)\]', {
    param($m)
    $token = "__WORD_LINK_$tokenIndex__"
    $tokens[$token] = '<a href="' + (Html $m.Groups[1].Value) + '">' + (Html $m.Groups[1].Value) + '</a>'
    $tokenIndex++
    return $token
  })
  $encoded = Html $normalized
  $encoded = [regex]::Replace($encoded, 'https?://[^\s<>\]\)"''，。；]+', {
    param($m)
    $url = $m.Value
    return '<a href="' + $url + '">' + $url + '</a>'
  })
  foreach ($token in $tokens.Keys) { $encoded = $encoded.Replace((Html $token), $tokens[$token]) }
  return $encoded.Replace("`n", '<br>')
}

function ParagraphHtml([string]$Text) {
  $body = Linkify $Text
  if ($body.StartsWith('省時版本：')) {
    $body = '<strong>省時版本：</strong>' + $body.Substring(('省時版本：').Length)
  }
  return '<p>' + $body + '</p>'
}

function TableHtml([System.Xml.XmlNode]$Table) {
  $rows = New-Object System.Collections.Generic.List[string]
  $rowIndex = 0
  foreach ($row in $Table.SelectNodes('./w:tr', $ns)) {
    $cells = New-Object System.Collections.Generic.List[string]
    $cellTag = if ($rowIndex -eq 0) { 'th' } else { 'td' }
    foreach ($cell in $row.SelectNodes('./w:tc', $ns)) {
      $cellText = (($cell.SelectNodes('./w:p', $ns) | ForEach-Object { Get-SequenceText $_ }) -join "`n")
      [void]$cells.Add('<' + $cellTag + '>' + (Linkify $cellText) + '</' + $cellTag + '>')
    }
    [void]$rows.Add('<tr>' + ($cells -join '') + '</tr>')
    $rowIndex++
  }
  if ($rows.Count -eq 0) { return '' }
  return '<table><thead>' + $rows[0] + '</thead><tbody>' + (($rows | Select-Object -Skip 1) -join '') + '</tbody></table>'
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
  $parent = Split-Path -Parent $Path
  if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
  [System.IO.File]::WriteAllText($Path, $Content, (New-Object System.Text.UTF8Encoding($false)))
}

$zip = [System.IO.Compression.ZipFile]::OpenRead($DocxPath)
try {
  $stylesEntry = $zip.GetEntry('word/styles.xml')
  $stylesReader = New-Object System.IO.StreamReader($stylesEntry.Open())
  $stylesXml = New-Object System.Xml.XmlDocument
  $stylesXml.LoadXml($stylesReader.ReadToEnd())
  $stylesReader.Dispose()
  $styleNames = @{}
  foreach ($style in $stylesXml.SelectNodes('//w:style', $ns)) {
    $styleNames[(Get-AttrValue $style 'styleId')] = (Get-AttrValue $style.SelectSingleNode('./w:name', $ns) 'val').ToLowerInvariant()
  }

  $numberingEntry = $zip.GetEntry('word/numbering.xml')
  $numberingXml = New-Object System.Xml.XmlDocument
  if ($null -ne $numberingEntry) {
    $numberingReader = New-Object System.IO.StreamReader($numberingEntry.Open())
    $numberingXml.LoadXml($numberingReader.ReadToEnd())
    $numberingReader.Dispose()
  }
  $abstractFormats = @{}
  if ($null -ne $numberingEntry) {
    foreach ($abstract in $numberingXml.SelectNodes('//w:abstractNum', $ns)) {
      $id = Get-AttrValue $abstract 'abstractNumId'
      $fmtNode = $abstract.SelectSingleNode('./w:lvl[@w:ilvl="0"]/w:numFmt', $ns)
      $abstractFormats[$id] = if ($null -ne $fmtNode) { Get-AttrValue $fmtNode 'val' } else { '' }
    }
  }
  $numFormats = @{}
  if ($null -ne $numberingEntry) {
    foreach ($num in $numberingXml.SelectNodes('//w:num', $ns)) {
      $numId = Get-AttrValue $num 'numId'
      $abstractId = Get-AttrValue $num.SelectSingleNode('./w:abstractNumId', $ns) 'val'
      $numFormats[$numId] = $abstractFormats[$abstractId]
    }
  }

  $documentEntry = $zip.GetEntry('word/document.xml')
  $documentReader = New-Object System.IO.StreamReader($documentEntry.Open())
  $documentXml = New-Object System.Xml.XmlDocument
  $documentXml.LoadXml($documentReader.ReadToEnd())
  $documentReader.Dispose()

  $paragraphs = New-Object System.Collections.Generic.List[object]
  foreach ($p in $documentXml.SelectNodes('//w:body/w:p', $ns)) {
    $styleIdNode = $p.SelectSingleNode('./w:pPr/w:pStyle', $ns)
    $styleId = Get-AttrValue $styleIdNode 'val'
    $numIdNode = $p.SelectSingleNode('./w:pPr/w:numPr/w:numId', $ns)
    $numId = Get-AttrValue $numIdNode 'val'
    $text = Get-SequenceText $p
    $paragraphs.Add([pscustomobject]@{
      Node = $p
      Text = $text
      StyleId = $styleId
      Style = if ($styleNames.ContainsKey($styleId)) { $styleNames[$styleId] } else { '' }
      NumFormat = if ($numFormats.ContainsKey($numId)) { $numFormats[$numId] } else { '' }
    })
  }

  $meta = [ordered]@{}
  $internalLinks = New-Object System.Collections.Generic.List[object]
  $inInternalLinks = $false
  for ($i = 0; $i -lt $paragraphs.Count; $i++) {
    $text = $paragraphs[$i].Text.Trim()
    $next = if ($i + 1 -lt $paragraphs.Count) { $paragraphs[$i + 1].Text.Trim() } else { '' }
    if ($text -eq '594katchang-source.github.io 站內連結建議') { $inInternalLinks = $true; continue }
    if ($inInternalLinks -and $text -eq 'FAQ 與結構化資料建議') { $inInternalLinks = $false }
    if ($inInternalLinks -and $text -match '^(.+?)：(https://594katchang-source\.github\.io/\S+)$') {
      [void]$internalLinks.Add([ordered]@{ label = $Matches[1].Trim(); url = $Matches[2].Trim() })
    }
    if ($text -eq 'SEO 標題') { $meta.title = $next }
    elseif ($text.StartsWith('文章摘要：')) { $meta.excerpt = $text.Substring(5).Trim() }
    elseif ($text.StartsWith('目標搜尋字詞：')) { $meta.keywords = @($text.Substring(7).Trim() -split '、' | Where-Object { $_ }) }
    elseif ($text.StartsWith('建議 slug：')) { $meta.slug = $text.Substring(('建議 slug：').Length).Trim() }
    elseif ($text.StartsWith('建議 canonical：')) { $meta.canonical = $text.Substring(('建議 canonical：').Length).Trim() }
    elseif ($text.StartsWith('canonical：') -and -not $meta.canonical) { $meta.canonical = $text.Substring(('canonical：').Length).Trim() }
    elseif ($text.StartsWith('建議更新日期：')) { $meta.date = $text.Substring(7).Trim() }
    elseif ($text.StartsWith('作者：')) { $meta.author = $text.Substring(3).Trim() }
    elseif ($text.StartsWith('分類：')) { $meta.category = $text.Substring(3).Trim() }
    elseif ($text.StartsWith('標籤：')) { $meta.tags = @($text.Substring(3).Trim() -split '、' | Where-Object { $_ }) }
  }
  foreach ($required in @('title','excerpt','keywords','slug','canonical','date','category')) {
    if (-not $meta.Contains($required) -or [string]::IsNullOrWhiteSpace([string]$meta[$required])) { throw "Missing metadata: $required" }
  }

  $htmlParts = New-Object System.Collections.Generic.List[string]
  $active = $false
  $openList = ''
  function Flush-List {
    if ($script:openList) {
      [void]$script:htmlParts.Add('</' + $script:openList + '>')
      $script:openList = ''
    }
  }
  foreach ($child in $documentXml.SelectNodes('//w:body/*', $ns)) {
    if ($child.LocalName -eq 'p') {
      $record = $paragraphs | Where-Object { $_.Node -eq $child } | Select-Object -First 1
      $text = $record.Text.Trim()
      if ($record.Style -eq 'heading 1' -and $text -eq '正文') { $active = $true; continue }
      if ($record.Style -eq 'heading 1' -and $text -eq 'SEO 描述') { Flush-List; break }
      if (-not $active -or [string]::IsNullOrWhiteSpace($text)) { continue }
      if ($record.Style -eq 'heading 2') { Flush-List; [void]$htmlParts.Add('<h2>' + (Html $text) + '</h2>'); continue }
      if ($record.Style -eq 'heading 3') { Flush-List; [void]$htmlParts.Add('<h3>' + (Html $text) + '</h3>'); continue }
      $listTag = ''
      if ($record.Style -match 'list number' -or $record.NumFormat -eq 'decimal') { $listTag = 'ol' }
      elseif ($record.Style -match 'list bullet' -or $record.NumFormat -eq 'bullet') { $listTag = 'ul' }
      if ($listTag) {
        if ($openList -ne $listTag) { Flush-List; [void]$htmlParts.Add('<' + $listTag + '>'); $openList = $listTag }
        [void]$htmlParts.Add('<li>' + (Linkify $text) + '</li>')
      } else { Flush-List; [void]$htmlParts.Add((ParagraphHtml $text)) }
    } elseif ($child.LocalName -eq 'tbl' -and $active) {
      Flush-List
      [void]$htmlParts.Add((TableHtml $child))
    }
  }
  Flush-List
  $body = $htmlParts -join "`n"
  if ($internalLinks.Count -gt 0) {
    $related = New-Object System.Collections.Generic.List[string]
    foreach ($link in $internalLinks) {
      [void]$related.Add('<a href="' + (Html $link['url']) + '">' + (Html $link['label']) + '</a>')
    }
    $body += "`n<p><strong>延伸閱讀：</strong>" + (($related -join '、')) + '</p>'
  }

  $faq = New-Object System.Collections.Generic.List[object]
  $inFaq = $false
  for ($i = 0; $i -lt $paragraphs.Count; $i++) {
    $record = $paragraphs[$i]
    if ($record.Style -eq 'heading 2' -and $record.Text.Trim().StartsWith('FAQ：')) { $inFaq = $true; continue }
    if ($inFaq -and $record.Style -eq 'heading 2' -and -not $record.Text.Trim().StartsWith('FAQ：')) { break }
    if ($inFaq -and $record.Style -eq 'heading 3' -and $i + 1 -lt $paragraphs.Count) {
      $answer = $paragraphs[$i + 1]
      if ($answer.Style -notmatch 'heading' -and $answer.Text.Trim()) {
        [void]$faq.Add([ordered]@{ question = $record.Text.Trim(); answer = $answer.Text.Trim() })
      }
    }
  }

  $visible = [regex]::Replace($body, '<[^>]+>', '')
  $visible = [regex]::Replace($visible, '\s', '')
  $post = [ordered]@{}
  $post['id'] = [string]$meta['slug']
  $post['title'] = [string]$meta['title']
  $post['date'] = [string]$meta['date']
  $post['category'] = [string]$meta['category']
  $post['excerpt'] = [string]$meta['excerpt']
  $post['keywords'] = @($meta['keywords'])
  $post['showOnHome'] = $false
  $post['body'] = [string]$body
  $post['faq'] = @($faq | ForEach-Object { $_ })
  $manifest = [ordered]@{}
  $manifest['source_docx'] = (Resolve-Path $DocxPath).Path
  $manifest['source_docx_sha256'] = (Get-FileHash -Algorithm SHA256 -LiteralPath $DocxPath).Hash
  $manifest['post_id'] = [string]$post['id']
  $manifest['title'] = [string]$post['title']
  $manifest['date'] = [string]$post['date']
  $manifest['canonical'] = [string]$meta['canonical']
  $manifest['visible_characters'] = $visible.Length
  $manifest['body_html_bytes'] = [Text.Encoding]::UTF8.GetByteCount($body)
  $manifest['faq_count'] = $faq.Count
  $manifest['body_table_count'] = ([regex]::Matches($body, '<table>')).Count
  $manifest['body_h2_count'] = ([regex]::Matches($body, '<h2>')).Count
  $manifest['body_h3_count'] = ([regex]::Matches($body, '<h3>')).Count
  $manifest['internal_link_count'] = $internalLinks.Count
  Write-Utf8NoBom $OutputJson (($post | ConvertTo-Json -Depth 8) + "`n")
  Write-Utf8NoBom $OutputHtml ($body + "`n")
  Write-Utf8NoBom $ManifestPath (($manifest | ConvertTo-Json -Depth 8) + "`n")
  $manifest | ConvertTo-Json -Depth 8
} finally {
  $zip.Dispose()
}
