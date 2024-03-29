l1=[]

def count(n):
    if n==0:
        return
    count(n-1)
    l1.append(n)
    return l1


print(count(5))