class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        xor=0
        if nums.count(0)==n:
                return 0
        for i in nums:
            xor^=i
        if xor==0:
            return n-1
        else:
            return n
             

        