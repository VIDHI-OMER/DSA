class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini=min(nums)
        moves=0
        for i in nums:
            moves+=i-mini
        return moves
