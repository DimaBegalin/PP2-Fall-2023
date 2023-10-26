def even_n(n):
    return (str(x) for x in range(1, n+1, 2))

n = int(input())
res = even_n(n)


res_str = ', '.join(res)
print(res_str)