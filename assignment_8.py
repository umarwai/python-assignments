# Assignment #8

# Task 1
float_strings = ["1.5", "2.8", "3.0"]
total = 0
for s in float_strings:
    total += float(s)
print("Sum:", total)

# Task 2
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Task 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = a + b
print("Sum:", result)
print("Type:", type(result))

# Task 4
items = ["5", 8, 10.5, True]
for i in range(len(items)):
    if type(items[i]) == str:
        items[i] = int(items[i])
print("Updated list:", items)

# Task 5
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
total = m1 + m2 + m3
percentage = (total / 300) * 100
print("Total:", total)
print("Percentage:", percentage)

# Task 6
s = "4.2"
val = float(s) * 2
if val > 5:
    print("Result is greater than 5")

# Task 7
marks = ["60", "40", "25", "90"]
for m in marks:
    if int(m) >= 50:
        print(m, "Pass")
    else:
        print(m, "Fail")

# Task 8
email = input("Enter email: ")
if "@" in email:
    print("Valid")
else:
    print("Invalid")

# Task 9
sentence = input("Enter a sentence: ")
count = sentence.lower().count("the")
print("Count of 'the':", count)

# Task 10
num_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for s in num_strings:
    n = int(s)
    if n % 2 == 0:
        print(n)
