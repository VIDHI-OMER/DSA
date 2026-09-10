class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t=len(target)
        l=[]
        j=0
        for i in range(1,n+1):
           
            l.append("Push")
            if i==target[j]:
                j+=1
                if j==t:
                    break
            else:
                l.append("Pop")
        return l
            



        