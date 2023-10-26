import math

n_sides = int(input("Input number of sides: "))
side_l = int(input("Input the length of a side: "))

area = int((n_sides * side_l ** 2) / (4 * math.tan(math.pi / n_sides)))
print(f"The area of the polygon is: {area}")
