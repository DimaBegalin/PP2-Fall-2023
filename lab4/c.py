a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(set(a) & set(b))
print(*c)
