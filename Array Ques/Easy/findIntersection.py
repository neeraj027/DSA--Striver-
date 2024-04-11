nums1=[4,9,5]
nums2=[9,4,9,8,4]

# temp=[]
n1=len(nums1)
n2=len(nums2)
i=0
j=0
temp=[]
while i<n1 and j<n2:
    if nums1[i]==nums2[j]:
        temp.append(nums1[i])
        i+=1
        j+=1
    elif nums1[i]<nums2[j]:
        j+=1
    else:
        i+=1
print(temp)