class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        opeen=0
        close=0
        if n%2==1:
            return False
        for i in range (n):
            if s[i]=='(' or locked[i]=='0':
                opeen+=1
            else:
                opeen-=1
            if opeen<0:
                return False
        for i in range (n-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                close+=1
            else:
                close-=1
            if close<0:
                return False
        return True