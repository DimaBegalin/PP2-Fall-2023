a = int(input())
b = int(input())
c = int(input())
res = 1

if a==b:
    res+=1
if b==c:
    res+=1
if a==c:
    res+=1
if res == 1 or res == 4:
    res-=1
print(res)
