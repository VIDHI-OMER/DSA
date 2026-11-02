class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m=0
        mid=nums[len(nums)//2]
        for i in nums:
            m+=abs(i-mid)
        return m
        