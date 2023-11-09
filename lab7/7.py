import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.sub(r'_', lambda finder: finder.group(1).upper(), readText)
print(n)