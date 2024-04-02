n=int(input())
arr=list(map(int,input().strip().split()))
hash1=[0]*len(arr)*2
search=int(input("-> "))

for i in range(n):
    hash1[arr[i]]+=1

for i in range(search):
    a=int(input("num: "))    
    print(hash1[a])

print(hash1)