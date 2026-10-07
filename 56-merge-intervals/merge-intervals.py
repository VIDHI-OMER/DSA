class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res=[]
        for i in intervals:
            if not res or i[0]>res[-1][1]:
                res.append(i)
            else:
                res[-1][1]=max(i[1],res[-1][1])
        return res


        
        
        