def recursiveinsertion(arr,n,i):
    if n==i:
        return
    j=i
    while (j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    recursiveinsertion(arr,n,i+1)

arr=[7,6,5,59,8,4,61,1]
n=len(arr)
recursiveinsertion(arr,n,0)
print(arr)