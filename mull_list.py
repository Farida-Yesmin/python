# Write a Python function to multiply all the numbers in a list.

def list_mull(a):
    mull = 1
    #a = list(map(int, input().split()))
    #print(a)
    for i in range(0, len(a)):
        mull *= a[i]
    return mull
a = list(map(int, input().split()))
print("Sample List: ", a)
summation = list_mull(a)
print("Expected output: ", summation)
