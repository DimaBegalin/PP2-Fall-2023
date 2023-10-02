s = list(map(int, input().split(" ")))
res = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i-1] and s[i] > s[i+1]:
        res+=1
print(res)
