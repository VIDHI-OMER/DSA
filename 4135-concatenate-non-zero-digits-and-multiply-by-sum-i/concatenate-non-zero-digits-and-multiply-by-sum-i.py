class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=''
        s=0
        n=str(n)
        for i in n:
            if i=='0':
                continue 
            else:
                x+=i
                s+=int(i)
        if x:
            return s*int(x)
        return s
    