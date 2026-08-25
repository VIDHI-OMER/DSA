class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        c=0
        ans=0
        for i in nums:
            if i==maxi:
                c+=1
                ans=max(ans,c)
            else:
                c=0
        return ans