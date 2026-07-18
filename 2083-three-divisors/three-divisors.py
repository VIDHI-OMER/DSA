class Solution:
    def isThree(self, n: int) -> bool:
        ct=0
        for i in range(1,n+1):
            if n%i==0:
                ct+=1
        #print(ct)
        if ct==3:
            return True
        return False
