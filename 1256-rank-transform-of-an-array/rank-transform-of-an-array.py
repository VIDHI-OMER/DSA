class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new=[]
        p=sorted(arr)
        #print(p)
        d={}
        c=0
        for i in range(len(p)):
            if p[i] not in d:
                d[p[i]]=c
                c+=1
        #print (p,d)
        for i in range(len(arr)):
            if arr[i] in d:
                new.append(d[arr[i]]+1)
        return new
    
        
    
            