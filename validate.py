import re, json

with open('data/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

print('Has BAMBOO_DATA:', 'BAMBOO_DATA' in content)
print('Has records:', '"Record_ID"' in content)
print('Has sources:', '"Source_ID"' in content)
print('File size:', len(content), 'bytes')

ids = re.findall(r'"B\d{3}"', content)
print('Record IDs found sample:', ids[:3], '...', ids[-3:])
print('Total Record_ID occurrences (should be 117):', len(ids)//2)  # each ID appears in key and value

# Check index.html has all 10 sections
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
sections = ['sec-home', 'sec-explore', 'sec-farmer', 'sec-workers', 'sec-transport', 'sec-market', 'sec-vc', 'sec-compare', 'sec-gaps', 'sec-sources']
for s in sections:
    print(f'Section {s} present:', s in html)
