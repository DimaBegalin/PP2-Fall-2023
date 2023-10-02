s = list(map(int, input().split(" ")))
k = int(input())

for i in range(len(s)):
    if k < i:
        s[i-1] = s[i]
s.pop()
for i in range(len(s)):
    print(s[i], end = ' ')
