class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n=len(nums)
        m=len(nums[0])
        sc=0
        
        for i in range(n):
            nums[i].sort(reverse=True)
        for col in range(m):
            mx=0
            for row in range(n):
                mx=max(mx,nums[row][col])
            sc+=mx
        return sc

        