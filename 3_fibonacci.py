#sum of fibonacci series

def fibonacci(num):
    
    sum, n1, n2 = 0, 0, 1
    print("the fibonacci series is:")
    for i in range(num):
        print(n1, end = " ")
        sum = sum + n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print("\nSummation of fibonacci series is: ", sum)
number = int(input("number: "))
fibonacci(number)
        
