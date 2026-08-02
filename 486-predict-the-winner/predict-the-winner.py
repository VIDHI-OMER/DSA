class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        tot=sum(nums)
        memo=[[-1]*n for _ in range(n)]
        def sol(i,j):
            if(i>j):
                return 0
            if(i==j):
                return nums[i]
            if memo[i][j]!=-1:
                return memo[i][j]
            takei=nums[i]+min(sol(i+2,j),sol(i+1,j-1))
            takej=nums[j]+min(sol(i,j-2),sol(i+1,j-1))
            memo[i][j]= max(takei,takej)
            return memo[i][j]
        p1=sol(0,n-1)
        p2=tot-p1
        return p1>=p2