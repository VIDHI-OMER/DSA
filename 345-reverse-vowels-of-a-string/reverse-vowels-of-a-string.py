class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        i=0
        j=n-1
        s=list(s)
        def isVow(ch):
            if ch in ['a','e','i','o','u','A','E','I','O','U']:
                return True
            return False
        while(i<j):
            if isVow(s[i])==False:
                i+=1
            if isVow(s[j])==False:
                j-=1
            if isVow(s[i]) and isVow(s[j]):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)


        