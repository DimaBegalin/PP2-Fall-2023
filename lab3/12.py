s = list(map(int, input().split(" ")))
k, c = map(int, input().split())

for i in range(len(s)):
    if k <= i:
        s[i], c = c, s[i]
s.append(c)
for i in range(len(s)):
    print(s[i], end = ' ')
