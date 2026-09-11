class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        one=0
        two=0
        for i in nums:
            s=str(i)
            if len(s)==1:
                one+=i
            else:
                two+=i
        return one!=two
        