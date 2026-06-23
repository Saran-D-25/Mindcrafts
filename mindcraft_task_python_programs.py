# ============================================
# MIND CRAFTS
# Python Programming Internship
# Core Python Challenges
# ============================================

# --------------------------------------------------
# 1. Sum of Two Numbers
# --------------------------------------------------
print("1. Sum of Two Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print("Sum =", sum_result)

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 2. Odd or Even Checker
# --------------------------------------------------
print("2. Odd or Even Checker")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 3. Factorial Calculation
# --------------------------------------------------
print("3. Factorial Calculation")
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 4. Fibonacci Sequence
# --------------------------------------------------
print("4. Fibonacci Sequence")
n = int(input("Enter the number of terms: "))

a, b = 0, 1
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 5. String Reverse
# --------------------------------------------------
print("5. String Reverse")
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 6. Palindrome Check
# --------------------------------------------------
print("6. Palindrome Check")
text = input("Enter a word or string: ")
reversed_text = text[::-1]

if text == reversed_text:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 7. Leap Year Check
# --------------------------------------------------
print("7. Leap Year Check")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:

    print(year, "is not a Leap Year")

print("\n" + "="*50 + "\n")


# --------------------------------------------------
# 8. Armstrong Number Check
# --------------------------------------------------
print("8. Armstrong Number Check")
num = int(input("Enter a number: "))

order = len(str(num))
sum_val = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if sum_val == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

print("\n" + "="*50)
