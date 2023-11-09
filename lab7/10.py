import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', readText)
print(n)