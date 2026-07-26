class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suf=1
        maxi=float('-inf')
        for i in nums:
            if(pre==0):
                pre=1
            pre=pre*i
            maxi=max(maxi,pre)
        for i in range(len(nums)-1,-1,-1):
            if(suf==0):
                suf=1
            suf=suf*nums[i]
            maxi=max(maxi,suf)
        return maxi
        