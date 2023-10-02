s = list(map(int, input().split(" ")))

minn = s[0]
maxx = s[0]

for i in range(len(s)):
    if s[i] > maxx:
        maxx = s[i]
    if s[i] < minn:
        minn = s[i]
for i in range(len(s)):
    if s[i] == maxx:
        print(minn, end = ' ')
    elif s[i] == minn:
        print(maxx, end = ' ')
    else:
        print(s[i], end = ' ')
