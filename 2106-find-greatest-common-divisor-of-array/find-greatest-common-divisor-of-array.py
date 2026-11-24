class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a=min(nums)
        b=max(nums)
        while a:
            a,b=b%a,a
            
        return b
        