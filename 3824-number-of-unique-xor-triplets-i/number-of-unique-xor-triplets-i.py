class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<=2):
            return n
        else:
            c=1
            while(c<=n):
                c*=2
            return c
        