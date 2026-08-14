class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i=1
        j=min(time)*totalTrips
        def check(mid):
            c=0
            for i in time:
                c+=mid//i
            return c
        while(i<j):
            mid=(i+j)//2
            if (check(mid)>=totalTrips):
                j=mid
            else:
                i=mid+1
        return i
            
        
        