nums=[1,2,3,4,5,6,7,8,9]
def revArr(l,r):
    if l>=r:
        return nums
    nums[l],nums[r]=nums[r],nums[l]
    revArr(l+1,r-1)
    
print(nums)
revArr(0,len(nums)-1)
print(nums)


#2nd method

def revArray2(i,n):
    if i>=n//2:
        return nums
    nums[i],nums[n-i]=nums[n-i],nums[i]
    revArray2(i+1,n)
    return nums

print(nums)
revArray2(0,len(nums)-1)
print(nums)
