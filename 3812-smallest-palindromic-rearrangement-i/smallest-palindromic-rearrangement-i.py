class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=n//2
        if n==1:
            return s
        l=sorted(s[:mid])
        if n%2==0:
            return ''.join(l+l[::-1])
        else:
            return ''.join(l+[s[mid]]+l[::-1])