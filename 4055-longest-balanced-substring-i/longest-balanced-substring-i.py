class Solution:
    def longestBalanced(self, s: str) -> int:
        maxi=0
        def check(f):
            c=0
            for i in range(26):
                if f[i]==0:
                    continue
                if c==0:
                    c=f[i]
                elif f[i]!=c:
                    return False
            return True
        for i in range(len(s)):
            f=[0]*26
            for j in range(i,len(s)):
                f[ord(s[j])-ord('a')]+=1
                if check(f):
                    maxi=max(maxi,j-i+1)
        return maxi
                