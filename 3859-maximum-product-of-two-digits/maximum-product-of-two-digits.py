class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while(n):
            rem=n%10
            l.append(rem)
            n=n//10
        print(l)
        maxi=0
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                maxi=max(maxi,l[i]*l[j])  
        return maxi      