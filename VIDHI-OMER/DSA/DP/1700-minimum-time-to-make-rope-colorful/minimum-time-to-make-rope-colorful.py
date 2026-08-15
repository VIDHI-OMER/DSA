class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        ans=0
        total=neededTime[0]
        maxi=neededTime[0]
        for i in range(1,len(colors)):
            if(colors[i]==colors[i-1]):
                total+=neededTime[i]
                maxi=max(maxi,neededTime[i])
            else:
                ans+=(total-maxi)
                total=neededTime[i]
                maxi=neededTime[i]
        ans+=total-maxi
        return ans
        
        