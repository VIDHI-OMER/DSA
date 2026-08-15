class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        c=0
        while(startValue!=target):
            if(startValue>target):
                c+=startValue-target
                return c
            if(target%2==0):
                c+=1
                target//=2
            else:
                c+=1
                target+=1
        return c
        
        