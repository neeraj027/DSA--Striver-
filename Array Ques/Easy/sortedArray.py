arr=[1,2,3,4,5,6,7,1]
n=len(arr)

def sortedArr(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return 0
    return 1

print(sortedArr(arr,n))