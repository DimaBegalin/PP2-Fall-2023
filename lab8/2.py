s = input()
upper, lower = sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())
print(f"Uppercase: {upper}\n Lowercase: {lower}")
