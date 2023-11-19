import os

p = input("Path to delete: ")

if os.access(p, os.F_OK) and os.access(p, os.W_OK):
    os.remove(p)
    print(f"Deleted: {p}")
else:
    print("ERROR")
