class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
       
        print(intervals)
        i=0
        while(i<len(intervals)-1):
            start=intervals[i][0]
            end=intervals[i][1]
            if intervals[i+1][0]<=end:
                intervals[i][1]=max(end,intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i+=1

        return intervals
        
        
        