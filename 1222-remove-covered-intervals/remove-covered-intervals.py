class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=0
        m=0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        print (intervals)
        for t,ed in intervals:
            if ed>m:
                c+=1
                m=ed
        return c
            
        