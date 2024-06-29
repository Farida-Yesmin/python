# Write a program to find the maximum between two numbers.


def compare(x,y):
    max = None
    if x>y:
        max = x
    else:
        max = y
    return max

a = int(input("Enter The value of X: "))
b = int(input("Enter The value of Y: "))

result = compare(a,b)

test ="The maximum number of {0} and {1} is {2}:"

print(test.format(a,b, result))
