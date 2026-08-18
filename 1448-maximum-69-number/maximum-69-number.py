class Solution:
    def maximum69Number (self, num: int) -> int:
        idx=-1
        c=0
        tmp=num
        while(tmp):
            rem=tmp%10
            if(rem==6):
                idx=c
            tmp//=10
            c+=1
        if (idx==-1):
            return num
        ans=num+3*(10**idx)
        return ans
        