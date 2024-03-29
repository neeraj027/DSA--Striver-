#Brute Force Method
n1=21
n2=6
gcd=1
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)


#Euclidian Algorithm
n=5
m=15
while n>0 and m>0:
        if n>m:
            n=n%m
        elif m>n:
            m=m%n
print(m if n==0 else n)