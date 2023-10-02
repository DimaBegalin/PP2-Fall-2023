s = list(map(int, input().split(" ")))
n = int(input())
res = len(s)+1
for i in range(len(s)):
    if s[i] < n:
        res = i + 1
        break
print(res)
