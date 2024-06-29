#Write a program to check whether a number is even or odd

n=int(input("Enter a value to check the number is even or odd: "))
print("\n")

if((n%2)==1):
    print("{0} is a odd Number".format(n))
    
else:
    print("{0} is a even Number".format(n))
