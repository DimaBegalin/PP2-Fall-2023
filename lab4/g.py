n = int(input())
res = []
out = []
l = []
result = []
while 1:
    s = input()
    if s == "HELP":
        break
    else:
        if s == "YES":
            if len(result) == 0:
                result = l
            else:
                result = list(set(result) & set(l))
        elif s == "NO":
            out.extend(l)
        else:
            l = list(map(int, s.split()))
result = sorted(list(set(result) - set(out)))
print(*result)
