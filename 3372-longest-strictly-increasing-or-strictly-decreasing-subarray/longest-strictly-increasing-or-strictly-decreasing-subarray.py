class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        inc=1
        dec=1
        res=1   
        
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                
                dec+=1
                inc=1
            elif nums[i+1]>nums[i]:
                inc+=1
                dec=1
            else:
                inc=dec=1
            
            res=max(inc,dec,res)
        return res


        