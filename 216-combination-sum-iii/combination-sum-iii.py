class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        l1=[]
        def fun(i,l,s):
            if s>n:
                return
            if i>=10:
                if s==n and len(l)==k:
                    l1.append(l[:])
                return
            s+=i
            l.append(i)
            fun(i+1,l,s)
            s-=i
            l.pop()
            fun(i+1,l,s)
        fun(1,[],0)
        return l1

        
        