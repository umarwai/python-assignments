# 1️⃣ Import math, use factorial(), create double(n) and call both
import math
def double(n):
    return n * 2
print("Factorial of 5:", math.factorial(5))
print("Double of 10:", double(10))

# 2️⃣ Use random.choice() on a list, define greet(name), use len()
import random
names = ["Ali", "Sara", "Zara", "Omar"]
print("Random name:", random.choice(names))
def greet(name):
    print("Hello", name)
greet("Umar")
print("List length:", len(names))

# 3️⃣ Use sum() and statistics.mean(), define is_even(num)
import statistics
marks = [60, 70, 80]
print("Total:", sum(marks))
print("Average:", statistics.mean(marks))
def is_even(num):
    return num % 2 == 0
print("Is 12 even?", is_even(12))

# 4️⃣ Import datetime, print current datetime, define say_hello(), use type()
import datetime
print("Now:", datetime.datetime.now())
def say_hello():
    print("Hello there!")
say_hello()
a = 100
print("Type of a:", type(a))

# 5️⃣ Create area_of_circle(radius) using math.pi and check type
def area_of_circle(radius):
    return math.pi * radius * radius
area = area_of_circle(5)
print("Area:", area)
print("Type of area:", type(area))

# 6️⃣ Import random, use randint(10,100), define check_number(num)
num = random.randint(10, 100)
print("Random number:", num)
def check_number(n):
    if n > 50:
        print("Greater than 50")
    else:
        print("50 or less")
check_number(num)

# 7️⃣ Use max() on list, math.pow(x, y), define display_info()
numbers = [12, 99, 43, 65]
print("Max number:", max(numbers))
print("2^3 =", math.pow(2, 3))
def display_info():
    name = "Ali"
    age = 18
    print("Name:", name)
    print("Age:", age)
display_info()

# 8️⃣ Import calendar, print May 2025, count characters, define show_message()
import calendar
print(calendar.month(2025, 5))
message = "Assignment 12 Completed"
print("Characters:", len(message))
def show_message():
    print("This is a message.")
show_message()

# 9️⃣ Import os, print current dir, convert int to str, define multiply(x, y)
import os
print("Current directory:", os.getcwd())
number = 123
str_number = str(number)
print("Converted:", str_number)
def multiply(x, y):
    return x * y
print("Product:", multiply(5, 4))

# 🔟 Define calculate_square_root(num), take input, convert to int, print sqrt
def calculate_square_root(num):
    return math.sqrt(num)
user_input = input("Enter a number: ")
n = int(user_input)
print("Type:", type(n))
print("Square root:", calculate_square_root(n))
