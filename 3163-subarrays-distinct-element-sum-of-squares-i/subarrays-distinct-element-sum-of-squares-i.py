class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            mp={}
            for j in range(i,n):
                if nums[j] not in mp:
                    mp[nums[j]]=1
                else:
                    mp[nums[j]]+=1
                s+=len(mp)**2
        return s

        