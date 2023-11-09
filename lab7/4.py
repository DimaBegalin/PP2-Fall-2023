import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.findall(r'[A-Z][a-z]+', readText)
print(n)