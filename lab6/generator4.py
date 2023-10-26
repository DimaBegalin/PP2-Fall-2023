def squares(a, b):
    for n in range(a, b + 1):
        yield n**2

a, b = map(int, input().split(" "))
for square in squares(a, b):
    print(square, end=' ')
