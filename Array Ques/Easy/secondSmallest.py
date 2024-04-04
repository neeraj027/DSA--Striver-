# arr=[5,3,8,6,1,6,25]
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
print(sorted(arr))
smallest=arr[0]
ssmallest=float("inf")

for i in range(n):
    if arr[i]<smallest:
        ssmallest=smallest
        smallest=arr[i]
    elif (arr[i]!=smallest and arr[i] < ssmallest ):
        ssmallest=arr[i]

print(ssmallest)