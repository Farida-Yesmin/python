
#Python program to find the power of any number

'''base, exponent, result = int(input("Enter the value of Base value: ")), int(input("Enter the value of Exponent value: ")), 1

for i in range(1, exponent+1):
    result *= base

print("\n\nThe power value of {0} and {1} is {2}".format(base, exponent, result))

'''


#use of while loop

base, exponent, result, i = int(input("Enter the value of Base value: ")), int(input("Enter the value of Exponent value: ")), 1, 1

while(i<exponent+1):        #or, while(i<=exponent)
    result *= base
    i += 1
    

print("\n\nThe power value of {0} and {1} is {2}".format(base, exponent, result))
