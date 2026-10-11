class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        lf=[]
        def suu(i,l,s):
            if s>target:
                return
            if i>=len(candidates):
                if s==target:
                    lf.append(l[:])
                return
            s+=candidates[i]
            l.append(candidates[i])
            suu(i,l,s)
            s-=candidates[i]
            l.pop()
            suu(i+1,l,s)
        suu(0,[],0)
        return lf

        