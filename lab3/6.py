s = list(map(int, input().split(" ")))
maxx = s[0]
ind = 0
for i in range(1, len(s)):
    if s[i] > maxx:
       maxx = s[i]
       ind = i
print(maxx, ind)
