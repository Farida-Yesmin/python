# Write a Python function to sum all the numbers in a list.

'''def list_sum():
    list= [1, 2, 3, 4, 6]
    sum = 0
    for i in range(0, len(list)):
        
        sum = sum+ list[i]

        return sum
a = list_sum()
print(a)
         
  '''
# 1.
'''def list_sum(list):
    list= [1, 2, 3, 4, 6]
    sum = 0
    for i in range(0, len(list)):
        sum = sum+ list[i]
    return sum
a = list_sum(list)
print(a)

'''
# 2.
'''num = input("enter numbers using spaces: ")
def answer(num):
num_list = num.split()
convert = [int(x) for x in num_list]
return convert
print (sum(answer(num_list)))
'''

'''num =input("Enter numbers using spaces: ")
def list_sum(num):
    num_list = num.split()
    convert = [int(x) for x in num_list]
    print(convert)
a= list_sum(num)
print(sum(a))'''


def list_sum(a):
    sum = 0
    #a = list(map(int, input().split()))
    #print(a)
    for i in range(0, len(a)):
        sum += a[i]
    return sum
a = list(map(int, input().split()))
print(a)
summation = list_sum(a)
print(summation)

        
        
































