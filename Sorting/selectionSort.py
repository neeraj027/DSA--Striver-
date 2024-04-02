arr=[3,5,4,7,9,55,6,1,32]# n=9
n=len(arr)
print(n)
print(arr)

for i in range(n):
    minIndex=i
    for j in range(i+1,n):
        if arr[j]<arr[minIndex]:
            minIndex=j

    arr[minIndex],arr[i]=arr[i],arr[minIndex]


print(arr)