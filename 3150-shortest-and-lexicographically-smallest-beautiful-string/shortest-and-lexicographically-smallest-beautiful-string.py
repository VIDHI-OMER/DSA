class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        for i in range(k,n+1):
            res=''
            for j in range(0,n-i+1):
                curr=s[j:j+i]
                if(curr.count('1')==k):
                    if(res=='' or curr<res):
                        res=curr
            if res:
                return res
        return ''
        