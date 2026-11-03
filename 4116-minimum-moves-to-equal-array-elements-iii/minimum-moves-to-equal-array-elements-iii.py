class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        move=0
        for i in nums:
            move+=maxi-i
        return move
        