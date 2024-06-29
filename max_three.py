
def max_two(x,y):
    if x>y:
        return x
    else:
        return y

def max_three(x, y, z):
    return max_two(x, max_two(y,z))

num1 = int(input("enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

a = max_three(num1, num2, num3)
print(a)
                   
