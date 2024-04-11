def linearSearch(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
arr=[1,2,9,4,0]
n=4
print(linearSearch(arr,n))