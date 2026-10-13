class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        print(nums)
        i=0
        j=n-1
        for k in range(n):
            if k%2==0:
                s+=nums[j]
                j-=1
            else:
                s-=nums[i]
                i+=1
        return s    