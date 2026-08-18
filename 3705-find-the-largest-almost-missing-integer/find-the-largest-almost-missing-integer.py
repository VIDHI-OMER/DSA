class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mp={}
        for i in range(n-k+1):
            seen=set()
            for j in range(i,i+k):
                if nums[j] not in seen:
                    mp[nums[j]]=mp.get(nums[j],0)+1
                    seen.add(nums[j])
        ans=-1
        for num in mp:
            if mp[num]==1:
                ans=max(ans,num)
        return ans