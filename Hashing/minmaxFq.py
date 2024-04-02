dict1={}
arr=[1,2,5,5,5,5,3,1,1,1]
n=len(arr)

for i in range(n):
    if arr[i] not in dict1:
        dict1[arr[i]]=1
    else:
        dict1[arr[i]]+=1


min1,max1=float("inf"),float("-inf")
minKey,maxKey=float("inf"),float("-inf")
for key,value in dict1.items():
    print("{0}->{1}".format(key,value))
    if value<min1:
        min1=value
        minKey=key
    if value>max1:
        max1=value
        maxKey=key
    if value==min1:
        minKey=min(minKey,key)
    if value==max1:
        maxKey=max(maxKey,key)

print(minKey,maxKey)