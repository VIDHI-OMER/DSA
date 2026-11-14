class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        res=float('inf')
        
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                if j-i+1>=l and j-i+1<=r and s>0:
                    res=min(res,s)
        if res==float('inf'):
            return -1
        return res
            
        