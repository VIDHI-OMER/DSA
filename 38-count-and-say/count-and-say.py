class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return '1'
        neww=self.countAndSay(n-1)
        res=''
        nn=len(neww)
        i=0
        while i<nn:
            ch=neww[i]
            c=1
            while(i<nn-1 and neww[i]==neww[i+1]):
                c+=1
                i+=1
            res+=str(c)+ch
            i+=1
        return res
