class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            i=0
            d=''
            while(i<len(s)):
                summ=0
                if i+k<=len(s):
                    for j in range(i,i+k):
                        summ+=int(s[j])
                    d+=str(summ)
                    i+=k
                else:
                    for j in range(i,len(s)):
                        summ+=int(s[j])
                        
                    d+=str(summ)
                    i=len(s)
            
            s=d
        return s
                


        