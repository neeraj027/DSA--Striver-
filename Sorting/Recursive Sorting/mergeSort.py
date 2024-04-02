class Solution:
    def divide(self,nums,low,high):
        if low==high:
            return
        mid=(low+high)//2
        self.divide(nums,low,mid)
        self.divide(nums,mid+1,high)
        self.merge(nums,low,mid,high)

    def merge(self,nums,low,mid,high):
        left=low
        right=mid+1
        temp=[]
        while(left<=mid and right<=high):
            if (nums[left]<=nums[right]):
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
            # print(temp)
        while left<=mid:
            temp.append(nums[left])
            left+=1
            # print(temp)
        while right<=high:
            temp.append(nums[right])
            right+=1
            # print(temp)
        for i in range(low,high+1):
            nums[i]=temp[i-low]

    def targetIndices(self, nums):
        low=0
        high=len(nums)-1
        self.divide(nums,low,high)
        return nums


arr=[1,2,5,2,3]
a=Solution()
print(a.targetIndices(arr))
