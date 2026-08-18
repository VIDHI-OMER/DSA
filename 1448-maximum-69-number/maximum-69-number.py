class Solution:
    def maximum69Number (self, num: int) -> int:
        maxi=num
        s=str(num)
        n=len(s)
        for i in range(n):
            if(s[i]=='6'):
                st=s.replace(s[i],'9',1)
                maxi=max(maxi,int(st))
            else:
                st=s.replace(s[i],'6',1)
                maxi=max(maxi,int(st))
        return maxi
        

        