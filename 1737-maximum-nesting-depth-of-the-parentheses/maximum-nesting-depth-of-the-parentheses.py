class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        stt=0
        for i in s:
            if i=='(':
                stt+=1
                maxi=max(maxi,stt)
            if i==')':
                stt-=1
        return maxi
            
        