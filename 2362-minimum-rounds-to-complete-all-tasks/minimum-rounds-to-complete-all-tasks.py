class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mp={}
        c=0
        for i in tasks:
            mp[i]=mp.get(i,0)+1
        for i,j in mp.items():
            if j<2:
                return -1
            if(j%3==0):
                c+=(j//3)
            else:
                c+=(j//3)+1
        return c