import os
import sys
import json
import truststore
truststore.inject_into_ssl()
import certifi
from google.oauth2 import service_account
from googleapiclient.discovery import build
import httplib2
import google_auth_httplib2
import ssl

BASE_DIR = r"d:\@Codex\594katchang-source.github.io-main"
CREDENTIALS_FILE = os.path.join(BASE_DIR, "gsc-credentials.json")
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = "https://594katchang-source.github.io/"

creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
ctx = ssl.create_default_context()
http = httplib2.Http()
http.ssl_context = ctx
authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
service = build('searchconsole', 'v1', http=authed_http)

# Check all-time pages
all_pages = service.searchanalytics().query(
    siteUrl=SITE_URL,
    body={'startDate': '2026-05-18', 'endDate': '2026-10-30', 'dimensions': ['page'], 'rowLimit': 100}
).execute().get('rows', [])

print("All-time pages:")
for p in all_pages:
    print(f"  {p['keys'][0]}: clicks={p.get('clicks')}, imp={p.get('impressions')}, ctr={p.get('ctr')*100:.2f}%, pos={p.get('position'):.2f}")

# Check all-time queries
all_queries = service.searchanalytics().query(
    siteUrl=SITE_URL,
    body={'startDate': '2026-05-18', 'endDate': '2026-10-30', 'dimensions': ['query'], 'rowLimit': 100}
).execute().get('rows', [])

print("\nAll-time queries:")
for q in all_queries:
    print(f"  {q['keys'][0]}: clicks={q.get('clicks')}, imp={q.get('impressions')}, ctr={q.get('ctr')*100:.2f}%, pos={q.get('position'):.2f}")

# Check October page+query combinations if any
oct_page_query = service.searchanalytics().query(
    siteUrl=SITE_URL,
    body={'startDate': '2026-10-01', 'endDate': '2026-10-30', 'dimensions': ['page', 'query'], 'rowLimit': 100}
).execute().get('rows', [])
print("\nOctober Page+Query:")
for pq in oct_page_query:
    print(f"  {pq['keys'][0]} | {pq['keys'][1]}: clicks={pq.get('clicks')}, imp={pq.get('impressions')}, ctr={pq.get('ctr')*100:.2f}%, pos={pq.get('position'):.2f}")

