def recuBubble(arr,n):
    didSwap=0
    if n==1:
        return
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            didSwap+=1
    if didSwap==0:
        return
    recuBubble(arr,n-1)


arr=[7,8,55,15,14,45,5,1,46]
n=len(arr)
print(arr)
recuBubble(arr,n)
print(arr)