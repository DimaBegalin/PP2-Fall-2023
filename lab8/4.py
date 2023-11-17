import time
from math import sqrt

n, m = map(int, input().split())
time.sleep(m / 1000)
output = sqrt(n)
print(f"Square root of {n} after {m} milliseconds is {output}")
