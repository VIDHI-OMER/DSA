class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr=[1,2,3,4,5,6,7,8,9]
        m=len(arr)
        l1=[]
        def fun(i,l,s):
            if s>n:
                return
            if i>=m:
                if s==n:
                    l1.append(l[:])
                return
            s+=arr[i]
            l.append(arr[i])
            fun(i+1,l,s)
            s-=arr[i]
            l.pop()
            fun(i+1,l,s)
        fun(0,[],0)
        res=[]
        for i in l1:
            if len(i)==k:
                res.append(i)
        return res

        
        