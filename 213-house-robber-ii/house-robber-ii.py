class Solution:
    def rob(self, nums: list[int]) -> int:
        #last and first are neighbours
        n=len(nums)
        d={}
        if n==1:
            return nums[0]
        def solve(i,m):
            if i>=m:
                return 0
            if (i,m) in d:
                return d[(i,m)]
            take=nums[i]+solve(i+2,m)
            nottake=solve(i+1,m)
            d[(i,m)]=max(take,nottake)
            return d[(i,m)]
        last=solve(0,n-1)
        first=solve(1,n)
        return max(last,first)
        