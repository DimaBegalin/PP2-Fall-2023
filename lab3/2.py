s = list(map(int, input().split(" ")))
for i in range(len(s)):
    if s[i] % 2 == 0:
        print(s[i], end = ' ')
