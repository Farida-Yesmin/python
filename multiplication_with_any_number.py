#1. Write a function that inputs a number
#and prints the multiplication table of that number


result, num = 1, int(input())

for i in range(1,11):
    result *= i
    
#print("\n\nThe power value of {0} and {1} is {2}".format(base, exponent, result))
print(result)
    
