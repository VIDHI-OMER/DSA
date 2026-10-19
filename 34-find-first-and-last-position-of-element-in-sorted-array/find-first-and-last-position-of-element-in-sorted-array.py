class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        def frt(i,j):
            fst=-1
            while(i<=j):
                mid=(i+j)//2
                if nums[mid]>=target:
                    if nums[mid]==target:
                        fst=mid
                    j=mid-1
                else:
                    i=mid+1
            return fst
        def lst(i,j):
            lnt=-1
            while(i<=j):
                mid=(i+j)//2
                if nums[mid]<=target:
                    if nums[mid]==target:
                        lnt=mid
                    i=mid+1
                else:
                    j=mid-1
            return lnt
        first=frt(0,n-1)
        last=lst(0,n-1)
        return [first,last]