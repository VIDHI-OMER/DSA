class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        l=[]
        def solve(i,l1):
            if i>n:
                if len(l1)==k:
                    l.append(l1[:])
                return 
            l1.append(i)
            solve(i+1,l1)
            l1.pop()
            solve(i+1,l1)
        solve(1,[])
        return l