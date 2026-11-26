class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=0
        time=10
        while(n>=time):
            if turn==0:
                n-=time
                turn=1
                time-=1
            else:
                n-=time
                turn=0
                time-=1
        return turn==1
        