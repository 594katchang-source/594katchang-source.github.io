import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open('work/2026-10-09-gsc-api-ranking-audit/output/gsc_full_official_data.json', encoding='utf-8'))

daily = [d for d in data['daily'] if d['impressions'] > 0 or d['clicks'] > 0]
print(f"Total active days with search impressions: {len(daily)}")
print("\nRecent 15 Active Days in Google Search:")
for d in daily[-15:]:
    dt = d['keys'][0]
    c = d['clicks']
    imp = d['impressions']
    pos = d['position']
    print(f"  {dt} -> Clicks: {c}, Impressions: {imp}, Avg Position: {pos:.1f}")

# Monthly aggregation
monthly = {}
for d in daily:
    month = d['keys'][0][:7]
    if month not in monthly:
        monthly[month] = {'clicks': 0, 'impressions': 0, 'positions': []}
    monthly[month]['clicks'] += d['clicks']
    monthly[month]['impressions'] += d['impressions']
    monthly[month]['positions'].append(d['position'])

print("\nMonthly Performance Summary:")
for m, stats in monthly.items():
    avg_p = sum(stats['positions']) / len(stats['positions']) if stats['positions'] else 0
    print(f"  {m} -> Clicks: {stats['clicks']}, Impressions: {stats['impressions']}, Avg Position: {avg_p:.1f}")
