class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n=len(skill)
        skill.sort()
        target=skill[0]+skill[-1]
        i=1
        j=n-2
        res=skill[0]*skill[-1]
        while(i<j):
            if skill[i]+skill[j]!=target:
                return -1
            res+=(skill[i]*skill[j])
            i+=1
            j-=1
        return res
