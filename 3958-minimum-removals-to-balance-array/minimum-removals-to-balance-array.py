class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=j=0
        maxi=nums[0]
        mini=nums[0]
        l=0
        while(j<len(nums)):
            maxi=nums[j]
            mini=nums[i]
            if maxi>k*mini:
                mini=nums[i]
                i+=1
            l=max(l,j-i+1)
            j+=1
        return len(nums)-l
        