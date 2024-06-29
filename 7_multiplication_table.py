#1. Write a function that inputs a number and prints the multiplication table of that number


'''num= int(input("Enter a value for Multiplication: "))
sum= 1

for i in range(1, 11):
    sum = num*i
    #print(sum)
    print("{0} * {1} = {2}".format(num, i, sum))
'''

def multiplication(num):
    sum= 1
    for i in range(1, 11):
        sum = num*i
        print("\n{0} X {1} = {2}".format(num, i, sum))

number = int(input("Enter a number as a multiplier: "))

multiplication(number)


