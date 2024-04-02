arr=[3,2,77,7,8,1,60,25,11]
# arr=[1,2,3,4]
n=len(arr)
print(arr)
swaps=0
for i in range(n):
    for j in range(n-1-i):
        if arr[j]>=arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swaps=1
    if swaps==0:
        break
print(arr)
