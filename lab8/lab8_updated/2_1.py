import os

p = input("Path: ")
d = [x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x))]
f = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p, x))]

print("Directories:", d)
print("Files:", f)
print("All:", os.listdir(p))
