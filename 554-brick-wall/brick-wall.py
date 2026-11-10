class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n=len(wall)
        mp={}
        for i in range(n):
            s=0
            for j in range(len(wall[i])-1):
                s+=wall[i][j]
                if s not in mp:
                    mp[s]=1
                else:
                    mp[s]+=1
       
        if not mp:
            return n
        return n-max(mp.values())
