class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while(n):
            rem=n%10
            l.append(rem)
            n=n//10
        print(l)
        l.sort()
        if len(l)==1:
            return l[0]
        else:
            return l[-1]*l[-2]