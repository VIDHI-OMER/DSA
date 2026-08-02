class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        tot=sum(nums)
        def sol(i,j):
            if(i>j):
                return 0
            if(i==j):
                return nums[i]
            takei=nums[i]+min(sol(i+2,j),sol(i+1,j-1))
            takej=nums[j]+min(sol(i,j-2),sol(i+1,j-1))
            return max(takei,takej)
        p1=sol(0,n-1)
        p2=tot-p1
        return p1>=p2