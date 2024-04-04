arr=[1,2,3,4,5]
n=len(arr)
print(arr)
# approach 1
# arr.append(arr.pop(0))
# print(arr)

# approach 2
temp=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[-1]=temp
print(arr)