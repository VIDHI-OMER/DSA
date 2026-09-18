class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        i=0
        j=0
        s=0
        minl=[float('inf')]*n
        res=float('inf')
        bestmini=float('inf')
        while(j<n):
            s+=arr[j]
            while(s>target):
                s-=arr[i]
                i+=1
            if s==target:
                l=j-i+1
                if i>0 and minl[i-1]!=float('inf'):
                    res=min(res,l+minl[i-1])
                bestmini=min(bestmini,l)
            minl[j]=bestmini
            j+=1
        if res!=float('inf'):
            return res
        return -1


        