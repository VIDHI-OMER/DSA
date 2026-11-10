class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n=len(nums)
        mp={}
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        for i in mp:
            if mp[i]>1:
                return i