# Assignment #7

# 1️⃣ Take user's full name and count characters
full_name = input("Enter your full name: ")
print("Total characters in your name:", len(full_name))

# 2️⃣ Print names with more than 5 characters
names = ["Ali", "Ahmed", "Sana", "Hassan", "Ayesha"]
print("Names with more than 5 characters:")
for name in names:
    if len(name) > 5:
        print(name)

# 3️⃣ Check if "python" is present in the sentence
sentence = input("Enter a sentence: ")
sentence_lower = sentence.lower()
if "python" in sentence_lower:
    print("The word 'python' is present.")
else:
    print("The word 'python' is not present.")

# 4️⃣ Print numbers divisible by 3
numbers = [2, 3, 6, 7, 9, 12, 15]
print("Numbers divisible by 3:")
for num in numbers:
    if num % 3 == 0:
        print(num)

# 5️⃣ Check if number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 6️⃣ Compare two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Greater number is:", num1)
else:
    print("Greater number is:", num2)

# 7️⃣ Add a city to the list
cities = ["Karachi", "Lahore", "Islamabad"]
new_city = input("Enter a new city name: ")
cities.append(new_city)
print("Updated city list:", cities)

# 8️⃣ Print each word in reverse order
words = ["apple", "banana", "grape", "mango", "orange"]
print("Words in reverse order:")
for i in range(4, -1, -1):
    print(words[i])

# 9️⃣ Take 3 marks and calculate total, average and grade
mark1 = int(input("Enter first mark: "))
mark2 = int(input("Enter second mark: "))
mark3 = int(input("Enter third mark: "))
total = mark1 + mark2 + mark3
average = total / 3
print("Total:", total)
print("Average:", average)

if average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# 🔟 Check if "apple" is in fruits list
fruits = ["banana", "apple", "grape", "mango"]
if "apple" in fruits:
    print("Found")
else:
    print("Not Found")
