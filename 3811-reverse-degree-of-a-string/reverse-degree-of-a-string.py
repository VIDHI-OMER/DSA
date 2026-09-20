class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        for i in range (len(s)):
            n=ord(s[i])-ord('a')
            rev=26-n
            c+=rev*(i+1)
        return c
            

        