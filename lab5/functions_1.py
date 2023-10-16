# Task 1
def task1(n):
    return n * 28.3495231

# Task 2
def task2(f):
    return ((f-32) * (5/9))


# Task 3
def task3(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None 

# Task  4
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(nums):
    return [x for x in nums if is_prime(x)]

# Task 5
from itertools import permutations

def print_perm(s):
    p = permutations(s)
    for i in p:
        print(''.join(i))

# Task 6
def reverse_sentence(input_string):
    w = input_string.split()
    r = ' '.join(w[::-1])
    return r

# Task 7
def has_3(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
# Task 8
def contains_007(lst):
    n = len(lst)
    i = 0
    for num in lst:
        if num == 0 and i == 0:
            i += 1
        elif num == 0 and i == 1:
            i += 1
        elif num == 7 and i == 2:
            return True
    return False
# Task 9
import math

def sphere_volume(r):
    return (4/3) * math.pi * r ** 3

# Task 10
def unique_list(l):
    unique = []
    for i in l:
        if i not in unique:
            unique.append(i)
    return unique
# Task 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
# Task 12
def histogram(d):
    for i in d:
        for _ in range(i):
            print('*', end='')
        print('')
# Task 13
import random

name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

number_to_guess = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Take a guess.\n"))
    attempts += 1

    if guess < number_to_guess:
        print("Your guess is too low.")
    elif guess > number_to_guess:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
        break







