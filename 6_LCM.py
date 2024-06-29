# 6. LCM


def calculate_lcm(num1, num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2
    for i in range(greater, (num1 *num2)+1):
        if (i%num1 == i%num2 ==0):
            lcm = i
            break
    return lcm

num1 = int(input("Enter first value: "))
num2 = int(input("Enter 2nd value: "))
print(f"\nThe LCM of {num1} and {num1} is: ", calculate_lcm(num1, num2))
        
