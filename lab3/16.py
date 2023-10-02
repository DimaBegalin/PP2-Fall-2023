q = []

for i in range(8):
    x, y = map(int, input().split())
    q.append((x, y))

res = "NO"

for i in range(7):
    for j in range(i + 1, 8):
        if q[i][0] == q[j][0] or q[i][1] == q[j][1] or abs(q[i][0] - q[j][0]) == abs(q[i][1] - q[j][1]):
            res = "YES"
            break

print(res)
