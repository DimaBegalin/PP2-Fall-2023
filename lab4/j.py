n, k = map(int, input().split())
pol = set()
for i in range(k):
    a_i, b_i = map(int, input().split())
    for j in range(a_i, n+1, b_i):
        if j % 7 == 6 or j % 7 == 0:
            continue
        else:
            pol.add(j)
print(len(set(pol)))
