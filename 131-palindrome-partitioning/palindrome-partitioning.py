class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        res=[]
        def isPal(st,ed):
            while(st<=ed):
                if s[st]!=s[ed]:
                    return False
                st+=1
                ed-=1
            return True
        def divide(idx,lt):
            if idx==n:
                res.append(lt[:])
                return
            for k in range(idx,n):
                if isPal(idx,k):
                    lt.append(s[idx:k+1])
                    divide(k+1,lt)
                    lt.pop()

        divide(0,[])
        return res