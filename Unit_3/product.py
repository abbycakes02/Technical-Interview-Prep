def compute(arr):
    # create result array
    prod = [1 for i in arr]
    temp = 1
    for i in range(0, len(arr)):
        prod[i] = temp
        temp*= arr[i]
    temp = 1
    for i in range(len(arr)- 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]
    return prod


    # prefix product of left side
    # prefix product of right right
# [1, 2, 2, 6]
# temp = 2
# temp = 2
# temp = 6
# temp = 18
arr = [2,1,3,3]
x = compute(arr)
print(x)