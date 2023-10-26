def div_generator(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a number: "))
for number in div_generator(n):
    print(number, end=' ')
