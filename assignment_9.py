# Assignment #9

# Task 1
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Task 2
ages = ["12", "18", "21", "16", "30"]
for age in ages:
    if int(age) >= 18:
        print(age)

# Task 3
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    print("Divisible by both 5 and 7")
elif num % 5 == 0:
    print("Divisible by 5")
elif num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 5 or 7")

# Task 4
numbers = ["3", "6", "9", "12"]
for n in numbers:
    if int(n) % 6 == 0:
        print(n)

# Task 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hello", name + ", you are an adult.")
else:
    print("Hello", name + ", you are a kid.")

# Task 6
nums = [10, 5, 20, 3, 15]
print("Max:", max(nums))
print("Min:", min(nums))

# Task 7
s = input("Enter digits in a string: ")
total = 0
for ch in s:
    if ch.isdigit():
        total += int(ch)
print("Sum of digits:", total)

# Task 8
password = input("Enter password: ")
if len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")

# Task 9
mixed = [10, "hello", 3.5, 7, True, "100"]
count = 0
for item in mixed:
    if type(item) == int:
        count += 1
print("Number of integers:", count)

# Task 10
import keyword
print("Total Python keywords:", len(keyword.kwlist))
