class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            d=''
            for i in range(0,len(s),k):
                grp=s[i:i+k]
                summ=0
                for j in grp:
                    summ+=int(j)
                d+=str(summ)
            s=d
        return s