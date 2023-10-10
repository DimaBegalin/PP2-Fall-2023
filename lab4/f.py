t = int(input())
s = ""
for i in range(t):
    s1 = input().replace('\n', ' ')
    s += ' ' + s1
res = s.strip().split(" ")
print(len(set(res)))
