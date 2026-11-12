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

BASE_DIR = r"d:\@Codex\594katchang-source.github.io-main"
CREDENTIALS_FILE = os.path.join(BASE_DIR, "gsc-credentials.json")
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = "https://594katchang-source.github.io/"

def get_service():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"[ERROR] Credentials file not found at {CREDENTIALS_FILE}")
        sys.exit(1)
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    return build('searchconsole', 'v1', http=authed_http)

def main():
    service = get_service()
    
    # 1. Probe all dates
    probe = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-05-01', 'endDate': '2026-11-01', 'dimensions': ['date'], 'rowLimit': 500}
    ).execute()
    
    date_rows = probe.get('rows', [])
    print(f"Total date points: {len(date_rows)}")
    if date_rows:
        print(f"Date range: {date_rows[0]['keys'][0]} to {date_rows[-1]['keys'][0]}")
        latest_date = date_rows[-1]['keys'][0]
    else:
        print("No date rows!")
        return

    # 2. September 2026 data
    sep_res = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-09-01', 'endDate': '2026-09-30'}
    ).execute().get('rows', [{}])[0]
    print(f"\nSeptember 2026: {sep_res}")

    # 3. October 2026 data (or available range in Oct)
    oct_end = min('2026-10-31', latest_date)
    oct_res = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end}
    ).execute().get('rows', [{}])[0]
    print(f"\nOctober 2026 (2026-10-01 to {oct_end}): {oct_res}")

    # 4. October Day-by-Day
    oct_daily = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end, 'dimensions': ['date'], 'rowLimit': 100}
    ).execute().get('rows', [])
    print(f"\nOctober Daily breakdown ({len(oct_daily)} days):")
    for r in oct_daily:
        print(f"  {r['keys'][0]}: clicks={r.get('clicks')}, imp={r.get('impressions')}, ctr={r.get('ctr')*100:.2f}%, pos={r.get('position'):.2f}")

    # 5. October Pages
    oct_pages = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end, 'dimensions': ['page'], 'rowLimit': 100}
    ).execute().get('rows', [])
    print(f"\nOctober Pages ({len(oct_pages)} pages):")
    for p in oct_pages:
        print(f"  {p['keys'][0]}: clicks={p.get('clicks')}, imp={p.get('impressions')}, ctr={p.get('ctr')*100:.2f}%, pos={p.get('position'):.2f}")

    # 6. September Pages for comparison
    sep_pages = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-09-01', 'endDate': '2026-09-30', 'dimensions': ['page'], 'rowLimit': 100}
    ).execute().get('rows', [])
    print(f"\nSeptember Pages ({len(sep_pages)} pages):")
    for p in sep_pages:
        print(f"  {p['keys'][0]}: clicks={p.get('clicks')}, imp={p.get('impressions')}, ctr={p.get('ctr')*100:.2f}%, pos={p.get('position'):.2f}")

    # 7. October Queries
    oct_queries = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end, 'dimensions': ['query'], 'rowLimit': 100}
    ).execute().get('rows', [])
    print(f"\nOctober Queries ({len(oct_queries)} queries):")
    for q in oct_queries:
        print(f"  {q['keys'][0]}: clicks={q.get('clicks')}, imp={q.get('impressions')}, ctr={q.get('ctr')*100:.2f}%, pos={q.get('position'):.2f}")

    # 8. October Devices
    oct_devices = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end, 'dimensions': ['device'], 'rowLimit': 10}
    ).execute().get('rows', [])
    print(f"\nOctober Devices:")
    for d in oct_devices:
        print(f"  {d['keys'][0]}: clicks={d.get('clicks')}, imp={d.get('impressions')}, ctr={d.get('ctr')*100:.2f}%, pos={d.get('position'):.2f}")

    # 9. October Countries
    oct_countries = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': oct_end, 'dimensions': ['country'], 'rowLimit': 20}
    ).execute().get('rows', [])
    print(f"\nOctober Countries:")
    for c in oct_countries:
        print(f"  {c['keys'][0]}: clicks={c.get('clicks')}, imp={c.get('impressions')}, ctr={c.get('ctr')*100:.2f}%, pos={c.get('position'):.2f}")

    # Save all raw results to json in output directory
    raw_output = {
        'date_range': {'start': '2026-10-01', 'end': oct_end, 'latest_in_gsc': latest_date},
        'sep_total': sep_res,
        'oct_total': oct_res,
        'oct_daily': oct_daily,
        'oct_pages': oct_pages,
        'sep_pages': sep_pages,
        'oct_queries': oct_queries,
        'oct_devices': oct_devices,
        'oct_countries': oct_countries
    }
    out_path = os.path.join(BASE_DIR, "work", "2026-11-01-october-marketing-performance-report", "output", "october_2026_gsc_raw_data.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(raw_output, f, ensure_ascii=False, indent=2)
    print(f"\nSaved raw data to {out_path}")

if __name__ == '__main__':
    main()
