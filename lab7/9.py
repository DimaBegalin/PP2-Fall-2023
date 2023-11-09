import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
x = re.sub(r'([A-Z][a-z]*)', r' \1', readText)
print(x)