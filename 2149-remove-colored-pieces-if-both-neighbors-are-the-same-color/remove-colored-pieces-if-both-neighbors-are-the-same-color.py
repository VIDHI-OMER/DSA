class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a=0
        b=0
        for i in range(1,len(colors)-1):
            char=colors[i]
            if colors[i-1]==char and colors[i+1]==char:
                if(char=='A'):
                    a+=1
                else:
                    b+=1
        if a==0 and b==0:
            return False
        if a>b:
            return True
        return False
        