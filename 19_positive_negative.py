#Write a program to check whether a number is negative, positive, or zero.


def positive_negtive(n):
    if n>0:
        return("{0} is a positive number". format(n))
    
    elif(n<0):
        return("{0} is a negative number". format(n))
        
    else:
        return("{0} is a Zero". format(n))
    
num = float(input("\n\nEnter a value to check the number is positive or negative: "))
print("\n")
print(positive_negtive(num))
