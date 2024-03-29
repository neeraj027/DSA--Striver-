def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return "YES" if count==2 else "NO"
    
n=6
print(prime(n))