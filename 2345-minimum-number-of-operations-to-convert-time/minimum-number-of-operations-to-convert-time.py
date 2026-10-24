class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current=current.split(':')
        correct=correct.split(':')
        
        curr_min=int(current[0])*60+int(current[1])
        corr_min=int(correct[0])*60+int(correct[1])

        req=corr_min-curr_min
        c=0
        for x in [60,15,5,1]:
            c+=req//x
            req%=x
        return c
            
