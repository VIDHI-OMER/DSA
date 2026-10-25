class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        aa=bin(a)[2:]
        bb=bin(b)[2:]
        s1=aa.count('1')
        s2=bb.count('1')
        if s1>=s2:
            score=s1*s2
            return score
        else:
            score=s2//s1
            return score
