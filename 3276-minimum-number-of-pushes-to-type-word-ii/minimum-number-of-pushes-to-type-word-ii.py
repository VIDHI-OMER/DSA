class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i,j in d.items():
            l.append(j)
        l.sort(reverse=True)
        print(l)
        res=0
        for i in range(len(l)):
            res+=l[i]*(i//8+1)
        return res
    
        
        