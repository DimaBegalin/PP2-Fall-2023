n1 = int(input())
n2 = int(input())
m1 = int(input())
m2 = int(input())

if n1 == m1 and n2 != m2 or n1 != m1 and n2 == m2:
    print("YES")
else:
    print("NO")