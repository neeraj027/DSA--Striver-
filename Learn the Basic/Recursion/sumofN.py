def sum(i,sum1):
    if i<1:
        print (sum1)
        return
    sum(i-1,sum1+i)

n=5
sum(n,0)