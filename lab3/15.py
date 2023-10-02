n, k = map(int, input().split())
s = ['I']*n
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l-1, r):
        s[j] = '.'
print("".join(s))
