class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        d={}
        def house(i):
            if i>=n:
                return 0
            if i in d:
                return d[i]
            take=nums[i]+house(i+2)
            nottake=0+house(i+1)
            d[i]=max(take,nottake)
            return d[i]
        return house(0)
