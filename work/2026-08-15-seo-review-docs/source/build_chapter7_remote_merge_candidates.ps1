param(
    [string]$Repo = '594katchang-source/594katchang-source.github.io',
    [string]$Ref = 'main',
    [string]$PostJsonPath = 'D:\@Codex\594katchang-source.github.io-main\work\2026-08-15-seo-review-docs\source\chapter-07-publish.json',
    [string]$PostsCandidatePath = 'D:\@Codex\594katchang-source.github.io-main\work\2026-08-15-seo-review-docs\source\remote-posts-candidate.json',
    [string]$SitemapCandidatePath = 'D:\@Codex\594katchang-source.github.io-main\work\2026-08-15-seo-review-docs\source\remote-sitemap-candidate.xml',
    [string]$SitemapHtmlCandidatePath = 'D:\@Codex\594katchang-source.github.io-main\work\2026-08-15-seo-review-docs\source\remote-sitemap-html-candidate.html',
    [string]$AuditPath = 'D:\@Codex\594katchang-source.github.io-main\work\2026-08-15-seo-review-docs\render\chapter-07-remote-merge-audit.json'
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

function Get-RemoteFile([string]$Path) {
    $endpoint = 'repos/' + $Repo + '/contents/' + $Path + '?ref=' + $Ref
    $responseText = (& gh api $endpoint --header 'Accept: application/vnd.github+json' --header 'User-Agent: Codex') -join "`n"
    if ($LASTEXITCODE -ne 0) { throw "Unable to read remote file through GitHub API: $Path" }
    $response = $responseText | ConvertFrom-Json
    $bytes = [Convert]::FromBase64String(($response.content -replace '\s', ''))
    [pscustomobject]@{
        content = [System.Text.Encoding]::UTF8.GetString($bytes)
        sha = [string]$response.sha
    }
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    [System.IO.File]::WriteAllText($Path, $Content, [System.Text.UTF8Encoding]::new($false))
}

$post = Get-Content -LiteralPath $PostJsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
$remotePosts = Get-RemoteFile 'blog/posts.json'
$remoteSitemap = Get-RemoteFile 'sitemap.xml'
$remoteSitemapHtml = Get-RemoteFile 'sitemap.html'
$postsDoc = $remotePosts.content | ConvertFrom-Json
$targetId = [string]$post.id

if (@($postsDoc.posts | Where-Object { $_.id -eq $targetId }).Count -gt 0) {
    throw "Target article already exists remotely: $targetId"
}
if ($post.showOnHome -ne $false) {
    throw 'Target article showOnHome must be false.'
}

$oldPostsById = @{}
foreach ($old in @($postsDoc.posts)) { $oldPostsById[[string]$old.id] = $old }
$postsDoc.posts = @($postsDoc.posts) + $post
$newPostsText = $postsDoc | ConvertTo-Json -Depth 30

$targetXmlUrl = 'https://594katchang-source.github.io/blog/post.html?id=2026-08-23-vitamins-book-notes'
$xml = $remoteSitemap.content
if ($xml.Contains($targetXmlUrl)) { throw 'Target article already exists in sitemap.xml.' }
$xmlEntry = "  <url>`n    <loc>$targetXmlUrl</loc>`n    <lastmod>2026-08-25</lastmod>`n    <changefreq>monthly</changefreq>`n    <priority>0.8</priority>`n  </url>`n"
if (-not $xml.Contains('</urlset>')) { throw 'sitemap.xml has no closing urlset.' }
$newXml = $xml.Replace('</urlset>', "$xmlEntry</urlset>")

$html = $remoteSitemapHtml.content
$targetHtmlId = '2026-08-23-vitamins-book-notes'
if ($html.Contains($targetHtmlId)) { throw 'Target article already exists in sitemap.html.' }
$safeTitle = [System.Net.WebUtility]::HtmlEncode([string]$post.title)
$safeExcerpt = [System.Net.WebUtility]::HtmlEncode([string]$post.excerpt)
$htmlEntry = '        <li class="sitemap-item"><a href="' + $targetXmlUrl + '">衛教：' + $safeTitle + '</a><p class="sitemap-desc">【2026-08-23】' + $safeExcerpt + '</p></li>'
$chapter6Pattern = '(?s)<li class="sitemap-item"><a href="[^"]*2026-08-22-proteins-amino-acids-book-notes[^"]*">.*?</li>'
$chapter6Match = [regex]::Match($html, $chapter6Pattern)
if (-not $chapter6Match.Success) { throw 'Chapter 6 entry was not found in sitemap.html.' }
$newHtml = $html.Insert($chapter6Match.Index + $chapter6Match.Length, "`n$htmlEntry")

Write-Utf8NoBom $PostsCandidatePath $newPostsText
Write-Utf8NoBom $SitemapCandidatePath $newXml
Write-Utf8NoBom $SitemapHtmlCandidatePath $newHtml

$newPostsDoc = $newPostsText | ConvertFrom-Json
$newNonTarget = @($newPostsDoc.posts | Where-Object { $_.id -ne $targetId })
$oldIds = @($oldPostsById.Keys | Sort-Object)
$newIds = @($newNonTarget | ForEach-Object { [string]$_.id } | Sort-Object)
$nonTargetIdsPreserved = (@($oldIds) -join "`n") -eq (@($newIds) -join "`n")
$nonTargetObjectsPreserved = $true
foreach ($newItem in $newNonTarget) {
    $oldItem = $oldPostsById[[string]$newItem.id]
    if (($oldItem | ConvertTo-Json -Depth 30 -Compress) -ne ($newItem | ConvertTo-Json -Depth 30 -Compress)) {
        $nonTargetObjectsPreserved = $false
        break
    }
}
$oldHomeCount = @($oldPostsById.Values | Where-Object { $_.showOnHome -eq $true }).Count
$newHomeCount = @($newPostsDoc.posts | Where-Object { $_.showOnHome -eq $true }).Count

$audit = [ordered]@{
    repo = $Repo
    ref = $Ref
    remote_posts_sha = $remotePosts.sha
    remote_sitemap_sha = $remoteSitemap.sha
    remote_sitemap_html_sha = $remoteSitemapHtml.sha
    target_id = $targetId
    old_post_count = @($oldPostsById.Keys).Count
    new_post_count = @($newPostsDoc.posts).Count
    target_show_on_home = [bool]$post.showOnHome
    old_home_count = $oldHomeCount
    new_home_count = $newHomeCount
    non_target_ids_preserved = $nonTargetIdsPreserved
    non_target_objects_preserved = $nonTargetObjectsPreserved
    target_in_posts = @($newPostsDoc.posts | Where-Object { $_.id -eq $targetId }).Count
    target_in_sitemap_xml = ([regex]::Matches($newXml, [regex]::Escape($targetXmlUrl))).Count
    target_in_sitemap_html = ([regex]::Matches($newHtml, [regex]::Escape($targetHtmlId))).Count
    generated_files = @($PostsCandidatePath, $SitemapCandidatePath, $SitemapHtmlCandidatePath)
}
Write-Utf8NoBom $AuditPath ($audit | ConvertTo-Json -Depth 10)
$audit | ConvertTo-Json -Depth 10
