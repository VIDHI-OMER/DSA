class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        while(i<j):
            mid=(i+j)//2
            if nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid
        def binary(i,j):
            while(i<=j):
                mid=(i+j)//2
                if nums[mid]<target:
                    i=mid+1
                elif nums[mid]>target:
                    j=mid-1
                else:
                    return mid
            return -1
        d=i
        lft=binary(0,d-1)
        rgt=binary(d,n-1)
        if lft!=-1:
            return lft
        if rgt!=-1:
            return rgt
        return -1
        