from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sm=min(nums)
        gr=max(nums)
        return gcd(sm,gr)
        