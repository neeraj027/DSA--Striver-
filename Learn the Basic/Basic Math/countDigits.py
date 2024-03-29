def countDigits(n):
    count=0
    while n>0:
        count+=1
        n=int(n/10)
    return count
    pass

print(countDigits(23250))