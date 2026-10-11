class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n+1):
            if n%(i+1)==0:
                s+=(nums[i]*nums[i])
        return s
        