class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        l=[]
        for i in range(left,right+1):

            number=i
            num=str(i)
            for j in range(len(num)):
                if num[j]=='0' or number%int(num[j])!=0:
                    break
            else:
                l.append(number)

        return l



        