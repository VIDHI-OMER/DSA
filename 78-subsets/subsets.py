class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        d=[]
        def sub(nums,i,l):
            if i>=len(nums):
                d.append(l[:])
                return
            l.append(nums[i])
            sub(nums,i+1,l)
            l.pop()
            sub(nums,i+1,l)
        sub(nums,0,[])
        return d
        