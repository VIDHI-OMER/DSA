class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        c=0
        tot=sum(nums)
        half=len(nums)//2
        halfS=sum(nums[0:half])
        for i in range(len(nums)):
            if halfS>tot-halfS:
                c+=1
            halfS-=nums[i]
            halfS+=nums[(i+half)%len(nums)]
            
        return c
