class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n=len(nums)
        d={}
        summ=sum(nums)
        target=summ//2
        if summ%2!=0:
            return False
        def solve(i,s):
            if s==target:
                return True
            if i==n:
                return False
            if (i,s) in d:
                return d[(i,s)]
            d[(i,s)]=solve(i+1,s+nums[i]) or solve(i+1,s)
            return d[(i,s)]
        return solve(0,0)

        