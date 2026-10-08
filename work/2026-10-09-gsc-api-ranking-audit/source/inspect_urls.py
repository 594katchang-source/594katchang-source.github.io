import os
import sys
import json
import truststore
truststore.inject_into_ssl()

import certifi
sys.stdout.reconfigure(encoding='utf-8')
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

from google.oauth2 import service_account
from googleapiclient.discovery import build
import httplib2
import google_auth_httplib2
import ssl

CREDENTIALS_FILE = r"d:\@Codex\594katchang-source.github.io-main\gsc-credentials.json"
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = "https://594katchang-source.github.io/"

urls_to_inspect = [
    "https://594katchang-source.github.io/",
    "https://594katchang-source.github.io/about.html",
    "https://594katchang-source.github.io/class.html",
    "https://594katchang-source.github.io/teach/nutritionranking/",
    "https://594katchang-source.github.io/teach/Stress-Food/",
    "https://594katchang-source.github.io/blog/post.html?id=2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health",
    "https://594katchang-source.github.io/blog/post.html?id=2026-08-22-proteins-amino-acids-book-notes"
]

def main():
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    service = build('searchconsole', 'v1', http=authed_http)
    
    results = []
    print("=== Inspecting Core URLs Index Status in Google Search Console ===")
    for url in urls_to_inspect:
        req = {
            'inspectionUrl': url,
            'siteUrl': SITE_URL
        }
        try:
            res = service.urlInspection().index().inspect(body=req).execute()
            idx_res = res.get('inspectionResult', {}).get('indexStatusResult', {})
            verdict = idx_res.get('verdict')
            coverage = idx_res.get('coverageState')
            crawled = idx_res.get('lastCrawlTime')
            canonical = idx_res.get('userCanonical')
            print(f"URL: {url}")
            print(f"  Verdict: {verdict} | Coverage: {coverage} | Last Crawl: {crawled}")
            results.append({
                'url': url,
                'verdict': verdict,
                'coverageState': coverage,
                'lastCrawlTime': crawled,
                'userCanonical': canonical,
                'full_res': res
            })
        except Exception as e:
            print(f"URL: {url} | Error: {e}")
            results.append({'url': url, 'error': str(e)})
            
    out_file = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-09-gsc-api-ranking-audit\output\url_inspection_results.json"
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved URL inspection results to: {out_file}")

if __name__ == "__main__":
    main()
