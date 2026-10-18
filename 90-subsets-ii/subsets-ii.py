class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        final=[]
        def sub(ind,l):
            final.append(l[:]) 
            for i in range(ind,n):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                l.append(nums[i])
                sub(i+1,l)
                l.pop()
        sub(0,[])
        return final