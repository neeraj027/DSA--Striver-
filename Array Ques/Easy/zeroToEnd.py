arr=[1,0,2,0,5,4,0,8,0,0,0,66,23]
n=len(arr)
print(arr)

#approach 1
# temp=[]
# for i in arr:
#     if i!=0:
#         temp.append(i)
# for i in range(len(temp)):
#     arr[i]=temp[i]

# for i in range(n-len(temp)):
#     arr[n-i-1]=0
# print(arr)

#approach 2
j=-1
for i in range(0,n):
    if arr[i]==0:
        j=i
        break

for i in range(j+1,n):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1




print(arr)