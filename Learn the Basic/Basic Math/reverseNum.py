def reverseNum(n):
    result=0
    while n>0:
        rem=int(n%10)
        result=result*10+rem
        n=int(n/10)
    return result

print(reverseNum(1234))