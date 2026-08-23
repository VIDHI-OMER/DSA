class Solution:
    def sumGame(self, num: str) -> bool:
        lftQ=0
        rgtQ=0
        n=len(num)
        mid=n//2
        lftSum=0
        rgtSum=0
        for i in range(n):
            if (i<mid):
                if(num[i]=='?'):
                    lftQ+=1
                else:
                    lftSum+=int(num[i])
            else:
                if(num[i]=='?'):
                    rgtQ+=1
                else:
                    rgtSum+=int(num[i])
        #print(lftQ,rgtQ,lftSum,rgtSum)
        diff=lftSum-rgtSum
        qdiff=lftQ-rgtQ

        if abs(qdiff) % 2 == 1:
            return True

        
        if qdiff == 0:
            return diff != 0

        
        return diff != -9 * (qdiff // 2)
