class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d=date.split('-')
        for i in range(len(d)):
            intt=int(d[i])
            binn=bin(intt)[2:]
            d[i]=binn
        #print(d)
        return '-'.join(d)