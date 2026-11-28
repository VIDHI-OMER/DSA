class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        mxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                c=0
            else:
                c+=1
            mxi=max(mxi,c)
        return mxi
        