a = list(map(int, input().split()))
b = []
for i in a:
    if i in b:
        print("YES")
    else:
        print("NO")
        b.append(i)
