class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        temp=[]
        temp.append([1])
        temp.append([1,1])
        if rowIndex<=1:
            return temp[rowIndex]
        for i in range(2,rowIndex+1):
            l=[1]*(i+1)
            for j in range(1,len(l)-1):
                l[j]=temp[i-1][j-1]+temp[i-1][j]
            temp.append(l)
        return temp[rowIndex]
            
