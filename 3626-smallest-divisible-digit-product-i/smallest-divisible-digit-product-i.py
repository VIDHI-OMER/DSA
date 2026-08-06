class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n,110):
            digipo=1
            num=i
            while(i):
                rem=i%10
                i=i//10
                digipo*=rem
            if(digipo%t==0):
                return num
            