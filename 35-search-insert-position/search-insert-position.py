class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]>target:
                j=mid-1
            elif nums[mid]<target:
                i=mid+1
            else:
                return mid
        return i
        