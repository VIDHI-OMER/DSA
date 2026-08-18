class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mp={}
        c=0
        for i in tasks:
            mp[i]=mp.get(i,0)+1
        for i,j in mp.items():
            if j<2:
                return -1
            
            c+=j//3
            j%=3
            if(j==1):
                c-=1
                c+=2
            elif j==2:
                c+=1
                    
        return c
        