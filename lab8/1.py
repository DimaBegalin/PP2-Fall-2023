from functools import reduce

n = list(map(int, input().split()))
result = reduce(lambda x, y: x * y, n)
print(result)
