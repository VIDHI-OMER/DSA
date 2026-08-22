class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        s=0
        p=1
        while(num):
            s+=(num%10)
            p*=(num%10)
            num//=10
        print(s,p)
        summ=s+p
        return n%summ==0
        
