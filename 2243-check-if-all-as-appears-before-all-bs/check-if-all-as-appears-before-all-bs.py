class Solution:
    def checkString(self, s: str) -> bool:
        lasta=-1
        firstb=-1
        for i in range(len(s)):
            if s[i]=='a':
                lasta=i
        for i in range(len(s)):
            if s[i]=='b':
                firstb=i
                break
        if lasta==-1 or firstb==-1:
            return True
        return lasta<firstb
        