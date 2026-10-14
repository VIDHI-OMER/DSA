class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9:
            return ""
        nine=sum//9
        rem=sum%9
        res=''
        for i in range(nine):
            res+='9'
        if rem>0:
            res+=str(rem)
        for i in range(num-len(res)):
            res+='0'
        return res