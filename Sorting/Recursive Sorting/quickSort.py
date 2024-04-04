def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    
    while i<j:
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def qS(arr,low,high):
    if low<high:
        pIndex=partition(arr,low,high)
        qS(arr,low,pIndex-1)
        qS(arr,pIndex+1,high)

arr=[10,5,2,11,32,0,1]
print(arr)
low=0
high=len(arr)-1
qS(arr,low,high)
print(arr)
