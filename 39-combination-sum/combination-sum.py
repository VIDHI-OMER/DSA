class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n=len(candidates)
        l1=[]
        def find(i,l,s): 
            if s>target:
                return
            if i>=n:
                if s==target:
                    l1.append(l[:])
                return
            s+=candidates[i]
            l.append(candidates[i])
            find(i,l,s)
            s-=candidates[i]
            l.pop()
            find(i+1,l,s)
        find(0,[],0)
        return l1

        