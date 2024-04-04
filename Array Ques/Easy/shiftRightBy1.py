arr=[1,2,3,4,5,6,7]
n=len(arr)

#approach 1
# arr=arr[-1:]+arr[:-1]
# print(arr)

#approach 2
# for i in range(1,n):
#     arr[n-i],arr[n-i-1]=arr[n-i-1],arr[n-i]
# print(arr)

#approach 3
temp=arr[-1]

for i in range(1,n):
    arr[n-i]=arr[n-i-1]
arr[0]=temp
print(arr)
