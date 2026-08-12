class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=j=0
        mp={}
        maxi=float('-inf')
        while (j<n):
            if nums[j] in mp:
                mp[nums[j]]+=1
            else:
                mp[nums[j]]=1
            while(mp[nums[j]]>k):
                mp[nums[i]]-=1
                if(mp[nums[i]]==0):
                    del mp[nums[i]]
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi