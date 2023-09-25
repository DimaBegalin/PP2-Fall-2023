n = int(input()) 
m = int(input()) 
x = int(input()) 
y = int(input())
x1 = x
x2 = max(n,m) - y
y1 = y
y2 = min(n,m) - x

print(min(x1, x2, y1, y2))
