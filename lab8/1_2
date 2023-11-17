import os

p = input("Path: ")
e = os.path.exists(p)
r, w, x = os.access(p, os.R_OK), os.access(p, os.W_OK), os.access(p, os.X_OK)

print(f"Path exists: {e}")
print(f"Readable: {r}")
print(f"Writable: {w}")
print(f"Executable: {x}")
