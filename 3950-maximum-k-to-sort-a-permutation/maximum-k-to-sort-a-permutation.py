class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        d=-1
        for i in range(len(nums)):
            if nums[i]!=i:
                d=d&nums[i]
        if d==-1:
            return 0
        return d

        