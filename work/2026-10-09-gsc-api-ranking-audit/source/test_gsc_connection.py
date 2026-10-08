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

CREDENTIALS_FILE = r"d:\@Codex\594katchang-source.github.io-main\gsc-credentials.json"
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

try:
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    
    # In httplib2, inject context with truststore
    import ssl
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    
    service = build('searchconsole', 'v1', http=authed_http)
    
    site_list = service.sites().list().execute()
    sites = site_list.get('siteEntry', [])
    print(f"[OK] Successfully authenticated with GSC API!")
    print(f"Total sites found: {len(sites)}")
    for s in sites:
        print(f"Site: {s.get('siteUrl')} | Permission: {s.get('permissionLevel')}")
        
    out_path = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-09-gsc-api-ranking-audit\output\sites_list.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sites, f, ensure_ascii=False, indent=2)
except Exception as e:
    import traceback
    print(f"[ERROR] Failed to connect to GSC API: {e}")
    traceback.print_exc()
    sys.exit(1)
