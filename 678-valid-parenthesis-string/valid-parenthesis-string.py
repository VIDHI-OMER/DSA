class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        opeen=0
        close=0
        
        for i in range (n):
            if s[i]=='(' or s[i]=='*':
                opeen+=1
            else:
                opeen-=1
            if opeen<0:
                return False
        for i in range (n-1,-1,-1):
            if s[i]==')' or s[i]=='*':
                close+=1
            else:
                close-=1
            if close<0:
                return False
        return True