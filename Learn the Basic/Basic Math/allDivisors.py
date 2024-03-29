def allDivisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

allDivisors(36)

print()

def allDivisors2(n):
    list1=[]
    i=1
    while i*i<=n:
        if n%i==0:
            list1.append(i)
            if n/i!=i:
                list1.append(int(n/i))
        i=i+1
    list1.sort()

    for i in list1:
        print(i,end=" ")
allDivisors2(36)