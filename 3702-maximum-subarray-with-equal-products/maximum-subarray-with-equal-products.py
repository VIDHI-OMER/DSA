from math import gcd

class Solution:
    def maxLength(self, nums):
        n=len(nums)
        ans=min(n, 2)
        left=0

        for right in range(n):
            for i in range(right):
                if gcd(nums[i],nums[right])>1:
                    left=max(left,i+1)

            ans=max(ans,right-left+1)

        return ans 