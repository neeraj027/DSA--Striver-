import math
def armstrongNum(n):
    dup=n
    count=int(math.log10(n))+1
    result=0
    while n>0:
        rem=int(n%10)
        n=int(n/10)
        result=result+rem**count
    return True if result==dup else False

print(armstrongNum(121))