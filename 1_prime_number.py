#Prime Numbers

def PrimeNumber(num):
    if(num == 2 or num%2 !=0):
        print(f"\n{num} is a prime number")
    else:

        print(f"\n{num} is not a prime number")
num = int(input("Enter a value to check is it prime or not: "))
PrimeNumber(num)
    
