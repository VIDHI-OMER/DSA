class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        i=j=0
        maxi=float('-inf')
        s=0
        while(j<n):
            s+=nums[j]
            if(s>maxi):
                maxi=max(maxi,s)
            if(s<0):
                s=0
            j+=1
        return maxi
            