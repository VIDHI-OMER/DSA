class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            d=nums[i]
            s=0
            while(d):
                rem=d%10 
                s+=rem
                d=d//10
            if s==i:
                return i
        return -1