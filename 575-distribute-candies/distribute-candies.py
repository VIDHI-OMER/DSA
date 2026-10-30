class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n=len(candyType)
        mp={}
        candy=n//2
        for i in candyType:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        return min(len(mp),candy)

        