class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        #firstly will find longest subarray whose sum is sum-x
        s=sum(nums)-x
        i=j=0
        maxi=float('-inf')
        summ=0
        if sum(nums)==x:
            return len(nums)
        if (sum(nums)<x):
            return -1
        while(j<len(nums)):
            summ+=nums[j]
            while(summ>s):
                summ-=nums[i]
                i+=1
            if summ==s:
                maxi=max(maxi,j-i+1)
            j+=1
        if maxi==float('-inf'):
            return -1
        return len(nums)-maxi
        


        