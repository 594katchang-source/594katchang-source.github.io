import csv
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"work\2026-10-02-gsc-performance-audit\data"

# 1. 讀取圖表.csv
chart_file = os.path.join(data_dir, "圖表.csv")
daily_data = []

with open(chart_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date_str = row['日期']
        clicks = int(row['點擊']) if row['點擊'] else 0
        impressions = int(row['曝光']) if row['曝光'] else 0
        ctr_str = row['點閱率'].replace('%', '') if row['點閱率'] else '0'
        ctr = float(ctr_str) if ctr_str else 0.0
        pos_str = row['排名']
        position = float(pos_str) if pos_str else None
        daily_data.append({
            'date': date_str,
            'clicks': clicks,
            'impressions': impressions,
            'ctr': ctr,
            'position': position
        })

monthly_stats = {}
for item in daily_data:
    month = item['date'][:7]
    if month not in monthly_stats:
        monthly_stats[month] = {
            'clicks': 0,
            'impressions': 0,
            'positions': [],
            'days_with_impressions': 0,
            'days_with_clicks': 0
        }
    monthly_stats[month]['clicks'] += item['clicks']
    monthly_stats[month]['impressions'] += item['impressions']
    if item['impressions'] > 0:
        monthly_stats[month]['days_with_impressions'] += 1
    if item['clicks'] > 0:
        monthly_stats[month]['days_with_clicks'] += 1
    if item['position'] is not None:
        monthly_stats[month]['positions'].append(item['position'])

print("=== 月度搜尋表現對比 ===")
for m in sorted(monthly_stats.keys()):
    st = monthly_stats[m]
    avg_pos = sum(st['positions']) / len(st['positions']) if st['positions'] else 0
    avg_ctr = (st['clicks'] / st['impressions'] * 100) if st['impressions'] > 0 else 0
    print(f"月份: {m}")
    print(f"  總曝光: {st['impressions']}, 總點擊: {st['clicks']}, CTR: {avg_ctr:.2f}%, 平均排名: {avg_pos:.2f}")
    print(f"  有曝光天數: {st['days_with_impressions']}, 有點擊天數: {st['days_with_clicks']}")

pre_sept_imp = sum(x['impressions'] for x in daily_data if x['date'] < '2026-09-01')
pre_sept_clicks = sum(x['clicks'] for x in daily_data if x['date'] < '2026-09-01')
sept_imp = sum(x['impressions'] for x in daily_data if x['date'] >= '2026-09-01')
sept_clicks = sum(x['clicks'] for x in daily_data if x['date'] >= '2026-09-01')

print(f"\n=== 改版前 (7-8月 63天) vs 改版推進後 (9月 29天) ===")
print(f"7-8月 每日平均曝光: {pre_sept_imp / 63:.2f}, 每日平均點擊: {pre_sept_clicks / 63:.2f}")
print(f"9月 每日平均曝光: {sept_imp / 29:.2f}, 每日平均點擊: {sept_clicks / 29:.2f}")
print(f"9月總點擊: {sept_clicks}, 9月總曝光: {sept_imp}")

pages_file = os.path.join(data_dir, "網頁.csv")
pages_data = []
with open(pages_file, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pages_data.append(row)

print("\n=== 熱門頁面表現 ===")
for p in pages_data:
    print(f"{p['熱門網頁']} | 點擊: {p['點擊']} | 曝光: {p['曝光']} | CTR: {p['點閱率']} | 排名: {p['排名']}")

dev_file = os.path.join(data_dir, "裝置.csv")
print("\n=== 裝置分佈 ===")
with open(dev_file, mode='r', encoding='utf-8-sig') as f:
    for line in f:
        print(line.strip())

country_file = os.path.join(data_dir, "國家_地區.csv")
print("\n=== 國家地區分佈 ===")
with open(country_file, mode='r', encoding='utf-8-sig') as f:
    for line in f:
        print(line.strip())
