class Solution:
    def candy(self, ratings: list[int]) -> int:
        n=len(ratings)
        demo=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                demo[i]=demo[i-1]+1
        #print(demo)
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                demo[i]=max(demo[i],demo[i+1]+1)
        #print(demo)
        return sum(demo)