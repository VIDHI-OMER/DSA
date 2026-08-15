class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        Allzero=True
        xor=0
        for i in nums:
            if i!=0:
                Allzero=False
            xor^=i
        if Allzero:
            return 0
        elif xor==0:
            return n-1
        else:
            return n
             

        