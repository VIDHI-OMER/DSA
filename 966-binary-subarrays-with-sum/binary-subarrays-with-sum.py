class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        mp={0:1}
        c=0
        s=0
        for i in nums:
            s+=i
            if s-goal in mp:
                c+=mp[s-goal]
            mp[s]=mp.get(s,0)+1
        return c