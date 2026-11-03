class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        moves=0
        for i in nums:
            if i%3==1 or i%3==2:
                moves+=1
        return moves