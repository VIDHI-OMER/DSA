class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        i=max(weights)
        j=sum(weights)
        ans=0
        def sol(mid):
            st=0
            day=1
            for i in weights:
                if(st+i<=mid):
                    st+=i
                else:
                    day+=1
                    st=i
            return day<=days

        while(i<=j):
            mid=(i+j)//2
            if sol(mid):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
        
            
        