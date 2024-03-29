def palindrome(n):
    dup=n
    result=0
    while n>0:
        rem=int(n%10)
        n=int(n/10)
        result=result*10+rem
    return True if result == dup else False

print(palindrome(12021))