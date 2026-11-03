"""Build the dependency-free offline page and CSV from the JSON catalogue."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
document = json.loads((ROOT / 'data/venues.json').read_text(encoding='utf-8'))
records = document['records']
assert len({r['id'] for r in records}) == len(records), 'Duplicate record IDs'
for row in records:
    assert row['level'] in ('A', 'B'), row['id']
    submission = row['submission']
    assert all(type(m) is int and 1 <= m <= 12 for m in submission['months']), row['id']
    assert submission['evidence'], row['id']

template = (ROOT / 'src/index.template.html').read_text(encoding='utf-8')
assert template.count('__DATA__') == 1
payload = json.dumps(records, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
(ROOT / 'index.html').write_text(template.replace('__DATA__', payload), encoding='utf-8')

def status(row):
    s = row['submission']
    if s['status'] == 'unverified' or s['confidence'] == 'low':
        return '仍需复核'
    return '常规投稿推断' if s.get('inferred') else '有官方日期／规则'

def cell(value):
    text = str(value or '')
    return "'" + text if text.startswith(('=', '+', '-', '@')) else text

with (ROOT / 'data/venues.csv').open('w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['简称', '全称', '类型', '等级', '分类', '目录序号', '出版社（PDF原文）', '目录网址', '官网/投稿说明', '大致投稿时间', '年份说明', '补充说明', '核查情况', 'PDF页码', '来源'])
    for row in records:
        s = row['submission']
        evidence = ' | '.join(f"{e.get('year', '')} {e.get('date', '')} {e['url']}" for e in s['evidence'])
        values = [row['short'], row['name'], row['type'], row['level'], row['category'], row['sequence'], row['publisher'], row['catalogueUrl'], row.get('officialUrl', ''), s['summary'], s.get('yearRelation', ''), s.get('notes', ''), status(row), row['pdfPage'], evidence]
        writer.writerow([cell(value) for value in values])
print(f'Built index.html and data/venues.csv from {len(records)} catalogue records.')
