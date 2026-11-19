class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        mini=arrays[0][0]
        maxi=arrays[0][-1]
        ans=0
        for i in range(1,len(arrays)):
            m=arrays[i][0]
            mx=arrays[i][-1]
            ans=max(ans,abs(m-maxi))
            ans=max(ans,abs(mx-mini))
            mini=min(mini,m)
            maxi=max(maxi,mx)
        return ans
