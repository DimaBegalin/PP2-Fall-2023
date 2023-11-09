import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.findall(r'[a-z]+_[a-z]+', readText)
print(n)