import re

f = open('row.txt', 'r', encoding='utf-8')
readText = f.read()
n = re.findall("ab*", readText)
print(n)