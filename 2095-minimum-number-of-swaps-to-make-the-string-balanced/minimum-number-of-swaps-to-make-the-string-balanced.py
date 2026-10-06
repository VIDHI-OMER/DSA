class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        opeen=0
        c=0
        for i in s:
            if i=='[':
                opeen+=1
            else:
                opeen-=1
                if opeen<0:
                    c+=1
                    opeen=1
        return c
