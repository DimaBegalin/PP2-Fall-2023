t = int(input())
stud = []
for i in range(t):
    n = int(input())
    l = []
    for j in range(n):
        l.append(input())
    stud.append(l)
res1 = []
res2 = []
for i in stud:
    if len(res1) == 0:
        res1 = set(i)
    else:
        res1 = set(res1 & set(i))
    if len(res2) == 0:
        res2 = set(i)
    else:
        res2 = set(res2 | set(i))
print(len(res1))
res1 = sorted(list(res1))
for i in res1:
    print(i)
print(len(res2))
res2 = sorted(list(res2))
for i in res2:
    print(i)
