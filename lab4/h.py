n = int(input())
possible = set(range(1, n + 1))

while True:
    q = input()
    if q == "HELP":
        break
    q_numbers = set(map(int, q.split()))
    yes = possible & q_numbers
    no = possible - q_numbers

    if len(yes) <= len(no):
        print("NO")
        possible = no
    else:
        print("YES")
        possible = yes

print(" ".join(map(str, sorted(list(possible)))))
