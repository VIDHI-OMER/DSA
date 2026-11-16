class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while(len(nums)>1):
            l=[0]*(len(nums)-1)
            for i in range(len(l)):
                sd=nums[i]+nums[i+1]
                l[i]=sd%10
            nums=l[:]
        return nums[0]