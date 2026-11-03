class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        mp={}
        for i in nums:
            pre=k-i
            if pre in mp:
                c+=1
                mp[pre]-=1
                if mp[pre]==0:
                    del mp[pre]
            else:
                mp[i]=mp.get(i,0)+1
        return c