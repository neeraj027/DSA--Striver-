arr=[5,3,8,6,1,6,25]
n=len(arr)

largest=arr[0]
secondLargest=float("-inf")

for i in range(n):
    if arr[i]>largest:
        secondLargest=largest
        largest=arr[i]
print(secondLargest)