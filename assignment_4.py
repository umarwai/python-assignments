# 1. Variables and arithmetic operations
a = 10
b = 3
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation
print(a // b)   # Floor division

# 2. Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 3. Boolean operations
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# 4. Assignment operations
num = 5
num += 3
print(num)
num -= 2
print(num)
num *= 4
print(num)
num /= 3
print(num)
num %= 3
print(num)
num **= 2
print(num)
num //= 2
print(num)

# 5. Identity operators
m = 100
n = 100
print(m is n)
print(m is not n)

# 6. Membership operators
text = "Python Programming"
print("Python" in text)
print("Java" not in text)

# 7. Print all Python keywords
import keyword
print(keyword.kwlist)

# 8. Variables and print values (no type())
name = "Ali"
age = 20
height = 5.9
print(name)
print(age)
print(height)

# 9. Valid and invalid variable names (invalid ones as comments)
# Valid:
user_name = "user"
x1 = 10
_value = 5
TotalAmount = 1000
data123 = [1,2,3]

# Invalid:
# 1name = "invalid"   # starts with a digit
# user-name = "invalid" # contains hyphen which is not allowed
# class = "invalid"  # reserved keyword

# 10. Special-naming variables
_hidden = 5
__private = 10
MAX_SIZE = 100
print(_hidden)
print(__private)
print(MAX_SIZE)

# 11. Assign values in one line
x, y, z = 1, 2, 3
print(x, y, z)

# 12. Assign same value to multiple variables
a = b = c = 0
print(a, b, c)

# 13. Delete variable example
temp = 100
print(temp)
del temp
# print(temp)   # This will cause an error because temp is deleted

# 14. String using triple single quotes
triple_single = '''Hello'''
print(triple_single)

# 15. Multi-line string using triple double quotes
multi_line = """This is line one.\nThis is line two."""
print(multi_line)

# 16. Checking data types with values only (no type)
integer_value = 10
float_value = 10.5
string_value = "Hello"
boolean_value = True
print(integer_value)
print(float_value)
print(string_value)
print(boolean_value)

# 17. Logical expression with score
score = 85
print(score > 50 and score < 100)

# 18. Membership test in string
message = "Welcome to Python"
print("Python" in message)
print("Python" not in message)

# 19. Code block with only comments explaining the program
# This program demonstrates use of variables,
# arithmetic operations, logical operators,
# membership and identity operators,
# and string manipulation in Python.

# 20. Print memory address using id()
data = 123
print(id(data))
