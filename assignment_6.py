# Assignment 6 - Loops, Conditions, Lists

# 1. Print numbers from 1 to 20 using a while loop
i = 1
while i <= 20:
    print(i)
    i += 1

# 2. Print every 3rd number from 3 to 30
for i in range(3, 31, 3):
    print(i)

# 3. Sum of even numbers from 2 to 20
sum_even = 0
for i in range(2, 21, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)

# 4. Product of odd numbers from 1 to 9
product = 1
for i in range(1, 10, 2):
    product *= i
print("Product of odd numbers:", product)

# 5. Print names from a list
names = ["Ali", "Sara", "John", "Emma", "Zain"]
for name in names:
    print(name)

# 6. Count 'a' in the word "banana"
word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print("Count of 'a':", count)

# 7. Print negative numbers from a list
numbers = [4, -2, 0, -7, 8, -1]
for num in numbers:
    if num < 0:
        print(num)

# 8. Numbers ending in 5 from 1 to 50
for i in range(1, 51):
    if i % 10 == 5:
        print(i)

# 9. Length of each word in list
words = ["cat", "elephant", "bat"]
for word in words:
    print(len(word))

# 10. Take 3 numbers and print average
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
avg = (n1 + n2 + n3) / 3
print("Average:", avg)

# 11. Table of 5 in reverse
for i in range(10, 0, -1):
    print("5 x", i, "=", 5 * i)

# 12. Print all characters in "Python Is Fun"
text = "Python Is Fun"
for char in text:
    print(char)

# 13. Print every second item in a list
items = [10, 20, 30, 40, 50, 60]
for i in range(0, len(items), 2):
    print(items[i])

# 14. Count consonants in a word from user
word = input("Enter a word: ")
count = 0
for letter in word:
    if letter.isalpha():
        if letter.lower() not in 'aeiou':
            count += 1
print("Number of consonants:", count)

# 15. Cubes of numbers from 1 to 5
for i in range(1, 6):
    print(i**3)

# 16. Words that start with 'a'
words = ["apple", "banana", "ant", "car", "aeroplane"]
for word in words:
    if word.startswith('a'):
        print(word)

# 17. Numbers from 100 to 110 excluding 105
for i in range(100, 111):
    if i != 105:
        print(i)

# 18. First 5 multiples of 4
for i in range(1, 6):
    print(4 * i)

# 19. Print each word in "Coding is easy"
sentence = "Coding is easy"
word1 = "Coding"
word2 = "is"
word3 = "easy"
print(word1)
print(word2)
print(word3)

# 20. Print only even numbers from a list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    if num % 2 == 0:
        print(num)
