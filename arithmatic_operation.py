'''Write a program to enter two numbers and perform all arithmetic
operations'''

num1 = int(input('Enter The First Number: '))
num2 = float(input('Enter The Second Number: '))

add, sub, mul, div, mod = 0, 0, 0, 0, 0

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2

print("\n")

print('The  Result of summation is:', num1, '+', num2, '=', add)
print('The  Result of Subtraction is:', num1, '-', num2, '=', sub)
print('The  Result of Multiplicatio is:', num1, '*', num2, '=', mul)
print('The  Result of Divition is:', num1, '/', num2, '=', div)
print('The  Result of Modulus is:', num1, '%', num2, '=', mod)
