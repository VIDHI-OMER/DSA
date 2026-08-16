class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        rem0=0
        rem1=0
        rem2=0
        for s in stones:
            rem=s%3
            if rem==0:
                rem0+=1
            elif rem==1:
                rem1+=1
            else:
                rem2+=1
        if rem0%2==0:
            return rem1>0 and rem2>0
        return abs(rem1-rem2)>2