class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s=str(num)
        n=len(s)
        for i in range(n):
            if(s[i]=='6'):
                st=s.replace(s[i],'9',1)
                return int(st)
        return num
        

        