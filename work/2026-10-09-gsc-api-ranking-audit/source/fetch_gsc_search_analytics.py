import os
import sys
import json
from datetime import datetime, timedelta
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

def get_service():
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    return build('searchconsole', 'v1', http=authed_http)

def main():
    service = get_service()
    
    # Try last 3 months (from 2026-07-01 to 2026-10-07)
    start_date = "2026-07-01"
    end_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    print(f"Querying GSC API for site: {SITE_URL}")
    print(f"Date range: {start_date} to {end_date}")
    
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': 5000,
        'dataState': 'all'  # Include fresh data if available
    }
    
    response = service.searchanalytics().query(siteUrl=SITE_URL, body=request).execute()
    rows = response.get('rows', [])
    print(f"Total query rows retrieved: {len(rows)}")
    
    out_dir = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-09-gsc-api-ranking-audit\output"
    out_file = os.path.join(out_dir, "gsc_all_queries.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
        
    print(f"Saved all queries to: {out_file}")
    
    # Print sample top queries
    print("\n--- Top 20 Queries by Impressions / Clicks ---")
    sorted_by_imp = sorted(rows, key=lambda x: x.get('impressions', 0), reverse=True)
    for r in sorted_by_imp[:20]:
        query = r.get('keys', [''])[0]
        clicks = r.get('clicks', 0)
        imp = r.get('impressions', 0)
        ctr = r.get('ctr', 0) * 100
        pos = r.get('position', 0)
        print(f"Query: {query:<30} | Clicks: {clicks:>3} | Imp: {imp:>5} | CTR: {ctr:>5.1f}% | Pos: {pos:>5.1f}")

if __name__ == "__main__":
    main()
