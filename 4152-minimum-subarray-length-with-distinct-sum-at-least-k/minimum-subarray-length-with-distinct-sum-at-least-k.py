class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        j=0
        mp={}
        s=0
        res=float('inf')
        while(j<n):
            if nums[j] not in mp:
                s+=nums[j]
                mp[nums[j]]=1
            else:
                mp[nums[j]]+=1
            while (s>=k):
                res=min(res,j-i+1)
                mp[nums[i]]-=1
                if(mp[nums[i]]==0):
                    s-=nums[i]
                    del mp[nums[i]]
                i+=1
            j+=1
        if res==float('inf'):
            return -1
        return res