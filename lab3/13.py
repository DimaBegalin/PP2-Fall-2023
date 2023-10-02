s = list(map(int, input().split(" ")))

res = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            res+=1
print(res)
