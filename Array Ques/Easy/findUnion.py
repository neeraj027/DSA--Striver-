a=[1,1,2,3,3,3,4,5]
b=[0,4,5,6,7,8,8,8,9]

#approach 1
# a=set(a)
# b=set(b)

# for i in b:
#     if i not in a:
#         a.add(i)
# print(sorted(a))

#approach 2
n1=len(a)
n2=len(b)
union=[]
i=0
j=0
while i<n1 and j<n2:
    if a[i]<=b[j]:
        if len(union)==0 or union[-1]!=a[i]:
            union.append(a[i])
        i+=1
    else:
        if len(union)==0 or union[-1]!=b[j]:
            union.append(b[j])
        j+=1
while i<n1:
    if len(union)==0 or union[-1]!=a[i]:
        union.append(a[i])
    i+=1

while j<n2:
    if len(union)==0 or union[-1]!=b[j]:
        union.append(b[j])
    j+=1

print(union)
