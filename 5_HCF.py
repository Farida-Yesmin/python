# 5. HCF

def calculate_hcf(num1, num2):
    #hcf = 1

    if num1>num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if(num1%i== num2%i== 0):
            hcf =i
            
    return hcf
first_num = int(input("Enter first value: "))

second_num = int(input("Enter second value: "))
print("\n")

print(f"HCF of {first_num} and {second_num} is : ", calculate_hcf(first_num, second_num))
    
