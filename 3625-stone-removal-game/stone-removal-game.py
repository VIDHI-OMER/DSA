class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn=0
        time=10
        while(n>=time):
            if turn==0:
                turn=1
            else:
                turn=0
            n-=time
            time-=1
        return turn==1
        