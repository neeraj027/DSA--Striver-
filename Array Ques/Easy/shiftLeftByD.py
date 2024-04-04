arr=[1,2,3,4,5,6,7]
n=len(arr)
d=1
print(arr)
if d>n:
    d=d%n

# print(d)

# temp=arr[0:d]
# print(temp)

# for i in range(d,n):
#     arr[i-d]=arr[i]

# for i in range(n-d,n):
#     arr[i]=temp[i-(n-d)]

# print(arr)


#approach 2
def reverseArr(arr,start,end):
    while(start<=end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    
reverseArr(arr,0,d-1)
reverseArr(arr,d,n-1)
reverseArr(arr,0,n-1)

print(arr)
