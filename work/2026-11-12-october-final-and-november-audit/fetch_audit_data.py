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
        body={'startDate': '2026-05-01', 'endDate': '2026-11-12', 'dimensions': ['date'], 'rowLimit': 500}
    ).execute()
    
    date_rows = probe.get('rows', [])
    print(f"Total date points: {len(date_rows)}")
    first_date = date_rows[0]['keys'][0]
    latest_date = date_rows[-1]['keys'][0]
    print(f"Date range: {first_date} to {latest_date}")

    # 2. September 2026 (baseline)
    sep_total = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-09-01', 'endDate': '2026-09-30'}
    ).execute().get('rows', [{}])[0]

    # 3. Full October 2026 (2026-10-01 to 2026-10-31)
    oct_total = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31'}
    ).execute().get('rows', [{}])[0]

    # 4. October daily
    oct_daily = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31', 'dimensions': ['date'], 'rowLimit': 100}
    ).execute().get('rows', [])

    # 5. October pages
    oct_pages = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31', 'dimensions': ['page'], 'rowLimit': 100}
    ).execute().get('rows', [])

    # 6. October queries
    oct_queries = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31', 'dimensions': ['query'], 'rowLimit': 100}
    ).execute().get('rows', [])

    # 7. October devices & countries
    oct_devices = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31', 'dimensions': ['device']}
    ).execute().get('rows', [])

    oct_countries = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': '2026-10-01', 'endDate': '2026-10-31', 'dimensions': ['country']}
    ).execute().get('rows', [])

    # 8. November 2026 (2026-11-01 to latest_date)
    nov_total = {}
    nov_daily = []
    nov_pages = []
    nov_queries = []
    if latest_date >= '2026-11-01':
        nov_total = service.searchanalytics().query(
            siteUrl=SITE_URL,
            body={'startDate': '2026-11-01', 'endDate': latest_date}
        ).execute().get('rows', [{}])[0]
        
        nov_daily = service.searchanalytics().query(
            siteUrl=SITE_URL,
            body={'startDate': '2026-11-01', 'endDate': latest_date, 'dimensions': ['date'], 'rowLimit': 100}
        ).execute().get('rows', [])

        nov_pages = service.searchanalytics().query(
            siteUrl=SITE_URL,
            body={'startDate': '2026-11-01', 'endDate': latest_date, 'dimensions': ['page'], 'rowLimit': 100}
        ).execute().get('rows', [])

        nov_queries = service.searchanalytics().query(
            siteUrl=SITE_URL,
            body={'startDate': '2026-11-01', 'endDate': latest_date, 'dimensions': ['query'], 'rowLimit': 100}
        ).execute().get('rows', [])

    # Print summary
    print(f"\n--- September 2026 ---")
    print(f"Clicks: {sep_total.get('clicks')}, Imp: {sep_total.get('impressions')}, CTR: {sep_total.get('ctr', 0)*100:.2f}%, Pos: {sep_total.get('position', 0):.2f}")

    print(f"\n--- Full October 2026 (10/01-10/31) ---")
    print(f"Clicks: {oct_total.get('clicks')}, Imp: {oct_total.get('impressions')}, CTR: {oct_total.get('ctr', 0)*100:.2f}%, Pos: {oct_total.get('position', 0):.2f}")

    print(f"\nOctober Pages:")
    for p in oct_pages:
        print(f"  {p['keys'][0]} | Clicks: {p.get('clicks')}, Imp: {p.get('impressions')}, CTR: {p.get('ctr', 0)*100:.2f}%, Pos: {p.get('position', 0):.2f}")

    print(f"\n--- November 2026 Month-to-date (11/01-{latest_date}) ---")
    print(f"Clicks: {nov_total.get('clicks')}, Imp: {nov_total.get('impressions')}, CTR: {nov_total.get('ctr', 0)*100:.2f}%, Pos: {nov_total.get('position', 0):.2f}")

    print(f"\nNovember Pages:")
    for p in nov_pages:
        print(f"  {p['keys'][0]} | Clicks: {p.get('clicks')}, Imp: {p.get('impressions')}, CTR: {p.get('ctr', 0)*100:.2f}%, Pos: {p.get('position', 0):.2f}")

    data = {
        'latest_date': latest_date,
        'sep_total': sep_total,
        'oct_total': oct_total,
        'oct_daily': oct_daily,
        'oct_pages': oct_pages,
        'oct_queries': oct_queries,
        'oct_devices': oct_devices,
        'oct_countries': oct_countries,
        'nov_total': nov_total,
        'nov_daily': nov_daily,
        'nov_pages': nov_pages,
        'nov_queries': nov_queries
    }

    out_file = os.path.join(BASE_DIR, "work", "2026-11-12-october-final-and-november-audit", "output", "gsc_full_audit_data.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\nSaved full data to {out_file}")

if __name__ == '__main__':
    main()
