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
OUTPUT_DIR = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-09-gsc-api-ranking-audit\output"

def get_service():
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    return build('searchconsole', 'v1', http=authed_http)

def main():
    service = get_service()
    
    # 1. Total Site Stats
    tot_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05'}
    tot_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=tot_req).execute()
    total_stats = tot_resp.get('rows', [{}])[0]
    
    # 2. Pages Breakdown
    pages_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05', 'dimensions': ['page'], 'rowLimit': 100}
    pages_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=pages_req).execute()
    pages_rows = pages_resp.get('rows', [])
    
    # 3. Daily Breakdown
    date_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05', 'dimensions': ['date'], 'rowLimit': 500}
    date_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=date_req).execute()
    date_rows = date_resp.get('rows', [])
    
    # 4. Queries Breakdown
    query_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05', 'dimensions': ['query'], 'rowLimit': 500}
    query_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=query_req).execute()
    query_rows = query_resp.get('rows', [])
    
    # 5. Devices Breakdown
    device_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05', 'dimensions': ['device'], 'rowLimit': 10}
    device_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=device_req).execute()
    device_rows = device_resp.get('rows', [])

    # 6. Countries Breakdown
    country_req = {'startDate': '2026-05-18', 'endDate': '2026-10-05', 'dimensions': ['country'], 'rowLimit': 20}
    country_resp = service.searchanalytics().query(siteUrl=SITE_URL, body=country_req).execute()
    country_rows = country_resp.get('rows', [])

    report_data = {
        'site_url': SITE_URL,
        'date_range': '2026-05-18 to 2026-10-05',
        'total_stats': total_stats,
        'pages': pages_rows,
        'daily': date_rows,
        'queries': query_rows,
        'devices': device_rows,
        'countries': country_rows
    }
    
    out_file = os.path.join(OUTPUT_DIR, 'gsc_full_official_data.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print(f"=== GSC Official Report Fetched Successfully ===")
    print(f"Total Impressions: {total_stats.get('impressions', 0)}")
    print(f"Total Clicks: {total_stats.get('clicks', 0)}")
    print(f"Overall CTR: {total_stats.get('ctr', 0)*100:.2f}%")
    print(f"Overall Average Position: {total_stats.get('position', 0):.2f}")
    print(f"\n--- Top Pages ---")
    for p in pages_rows:
        print(f"Page: {p['keys'][0]} | Clicks: {p['clicks']} | Imp: {p['impressions']} | Pos: {p['position']:.1f}")
        
    print(f"\n--- Devices ---")
    for d in device_rows:
        print(f"Device: {d['keys'][0]} | Clicks: {d['clicks']} | Imp: {d['impressions']} | Pos: {d['position']:.1f}")

    print(f"\n--- Countries ---")
    for c in country_rows:
        print(f"Country: {c['keys'][0]} | Clicks: {c['clicks']} | Imp: {c['impressions']}")

if __name__ == '__main__':
    main()
