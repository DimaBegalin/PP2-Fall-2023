import math
# Task 1
class StringManipulator:
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

# Task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Task 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"({self.x}, {self.y}"

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Task 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Task 6
def filter_prime(numbers):
    is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    return list(filter(is_prime, numbers))

if __name__ == "__main__":
    # Task 1
    s = StringManipulator()
    s.getString()
    s.printString()

    # Task 2
    square = Square(7)
    print(square.area())

    # Task 3
    rectangle = Rectangle(5, 3)
    print(rectangle.area())

    # Task 4
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(p1.show())
    p1.move(2, 3)
    print(p1.show())
    print(p1.dist(p2))

    # Task 5
    acc = Account("Arman", 1000)
    print(f"Account owner: {acc.owner}")
    print(f"Initial balance: {acc.balance}")
    acc.deposit(500)
    acc.withdraw(300)
    acc.withdraw(1500)
    print(f"Final balance: {acc.balance}")

    # Task 6
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    prime_numbers = filter_prime(numbers)
    print(prime_numbers)
