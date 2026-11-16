class Solution:
    def addDigits(self, num: int) -> int:
        nu=str(num)
        while (len(nu)>1):
            s=0
            num=int(nu)
            while(num):
                rem=num%10
                s+=rem
                num//=10
            nu=str(s)
        return int(nu)

            
        