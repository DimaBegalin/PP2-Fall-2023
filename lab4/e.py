n, m = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(m):
    x = int(input())
    b.append(x)
    c.append(x)
set_c = sorted(list(set(a) & set(b)))
set_a = sorted(list(set(a) - set(b)))
set_b = sorted(list(set(b) - set(a)))
print(len(set_c))
print(*set_c)
print(len(set_a))
print(*set_a)
print(len(set_b))
print(*set_b)
