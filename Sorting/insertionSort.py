arr=[85,655,2,45,32,6,64,4,7,354,545]
n=len(arr)
print(arr)

for i in range(n):
    j=i
    while (j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)