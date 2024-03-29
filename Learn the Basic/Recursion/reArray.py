nums=[1,3,5,8,7,9,5,45,5,66]
def revArr(l,r):
    if l>=r:
        return nums
    nums[l],nums[r]=nums[r],nums[l]
    revArr(l+1,r-1)
    
print(nums)
revArr(0,len(nums)-1)
print(nums)
