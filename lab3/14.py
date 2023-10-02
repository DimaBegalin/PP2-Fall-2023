s = list(map(int, input().split(" ")))
l = 0
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j] and i != j:
            l = 1
            break
    if l == 0:
        print(s[i], end = ' ')
    l = 0
