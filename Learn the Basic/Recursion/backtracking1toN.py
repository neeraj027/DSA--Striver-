def abc(i,n):
    if i<1:
        return
    abc(i-1,n)
    print(i)

    
n=3
abc(n,n)
