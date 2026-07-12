class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i=0
        j=len(nums)-1
        def BinarySearch1(i,j):
            fst=-1
            while(i<=j):
                mid=(i+j)//2
                if(nums[mid]>=target):
                    if(nums[mid]==target):
                        fst=mid
                    j=mid-1
                else:
                    i=mid+1
            return fst
        def BinarySearch2(i,j):
            snd=-1
            while(i<=j):
                mid=(i+j)//2
                if(nums[mid]<=target):
                    if(nums[mid]==target):
                        snd=mid
                    i=mid+1
                else:
                    j=mid-1
            return snd
        first=BinarySearch1(i,j)
        second=BinarySearch2(i,j)
        l=[]
        for i in range(first,second+1):
            if(nums[i]==target):
                l.append(i)
        return l


        
        