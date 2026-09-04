class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n=len(nums)
        mini=[0]*(n)
        maxi=[0]*(n)
        mini[n-1]=nums[n-1]
        maxi[0]=nums[0]
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])
        #print(maxi)
        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])
        #print(mini)
        for i in range(n):
            if maxi[i]-mini[i]<=k:
                return i
        return -1

        