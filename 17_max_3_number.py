# Write a program to find the maximum between three numbers.

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))
print("\n")

if(a>b and a>c):
    print("The greatest value is: ", a)
elif(b>a and b>c):
    print("The greatest value is: ", b)
else:
    print("The greatest value is: ", c)
