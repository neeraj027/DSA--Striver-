arr=[5,3,8,6,1,6,25]
n=len(arr)
largest=arr[0]
for i in range(1,n):
    if arr[i]>largest:
        largest=arr[i]
print(largest)