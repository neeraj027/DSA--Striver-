def reverseArr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def shiftRight(arr,n,d):
    d=d%n
    if d<0:
        d=n
    reverseArr(arr,0,n-d-1)
    reverseArr(arr,n-d,n-1)
    reverseArr(arr,0,n-1)

arr=[1,2,3,5]
n=len(arr)
d=2
shiftRight(arr,n,d)
print(arr)