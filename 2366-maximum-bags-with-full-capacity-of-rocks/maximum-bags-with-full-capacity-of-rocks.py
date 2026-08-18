class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(rocks)
        req=[]
        for i in range(n):
            req.append(capacity[i]-rocks[i])
        print(req)     
        req.sort()
        for i in range(len(req)):
            if req[i]>0 and req[i]<=additionalRocks:
                nd=req[i]
                req[i]=0
                additionalRocks-=nd
        return req.count(0)