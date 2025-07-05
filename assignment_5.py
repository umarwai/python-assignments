# 1️⃣ Check if number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2️⃣ Even or Odd
num = int(input("\nEnter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3️⃣ Check voting eligibility
age = int(input("\nEnter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 4️⃣ Check divisibility by 3 and 5
num = int(input("\nEnter a number to check divisibility: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# 5️⃣ Assign grade based on marks
marks = int(input("\nEnter student marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: Fail")

# 6️⃣ Weather check
temperature = float(input("\nEnter temperature in Celsius: "))
if temperature > 40:
    print("Too hot")
elif temperature < 10:
    print("Too cold")
else:
    print("Moderate weather")

# 7️⃣ Leap year check
year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 8️⃣ Find the largest of three numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 9️⃣ Password check
password = input("\nEnter password: ")
if password == "admin123":
    print("Access granted")
else:
    print("Access denied")

# 🔟 Integer check > 0 and < 100
num = int(input("\nEnter an integer: "))
if num > 0:
    print("Number is positive")
    if num < 100:
        print("Number is less than 100")
    else:
        print("Number is 100 or more")
else:
    print("Number is not positive")
