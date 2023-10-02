s = list(map(int, input().split(" ")))

for i in range(1, len(s)):
    if s[i] < 0 and s[i-1] < 0 or s[i] > 0 and s[i-1] > 0:
        print(s[i-1], s[i])
        break
