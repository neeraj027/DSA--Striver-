li=[]
n=7
c=1
def fact(c):
    if c>n:
        return
    li.append(c)
    print(c)
    fact(c*(len(li)+1))
    return(li)

print(fact(c))


# result=[]
# n=7
# def calculate_fact(current=1):

#     if current > n:

#         return

#     result.append(current)

#     calculate_fact(current * (len(result)+1))
#     return result
# print(calculate_fact())