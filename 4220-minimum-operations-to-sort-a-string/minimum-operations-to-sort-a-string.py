class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        mx=max(s)
        mi=min(s)
        print(sorted(s))
        if s==''.join(sorted(s)):
            return 0
        if n==2:
            return -1
        if s[0]==mi or s[-1]==mx:
            return 1
        for i in range(1,n-1):
            if s[i]==mx or s[i]==mi:
                return 2
        return 3

        