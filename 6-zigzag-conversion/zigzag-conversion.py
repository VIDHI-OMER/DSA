class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=[""]*numRows
        i=0
        if numRows==1:
            return s
        while(i<len(s)):
            for j in range(0,numRows):
                if i<len(s):
                    ans[j]+=s[i]
                    i+=1
            for k in range(numRows-2,0,-1):
                if i<len(s):
                    ans[k]+=s[i]
                    i+=1
        return ''.join(ans)


        