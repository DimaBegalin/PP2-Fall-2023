import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.sub(r'[ ,.]', ':', readText)
print(n)