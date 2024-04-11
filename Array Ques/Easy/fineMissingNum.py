#approach 1
arr=[0,1,2,3,4,6]
n=len(arr)

# hash1=[0]*(len(arr)+1)
# for i in range(n):
#     hash1[arr[i]]=1

# for i in range(len(hash1)):
#     if hash1[i]==0:
#         print(i)

#approach 2 - using sum of all

# num=0
# sum=(n*(n+1))//2
# for i in range(n):
#     num=num+arr[i]
# print(sum-num)

#approach 3 - using xor

xor1=0
xor2=0
for i in range(n):
    xor1=xor1 ^ i+1
    xor2=xor2 ^ arr[i]
print(xor1 ^ xor2)