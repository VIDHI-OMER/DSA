class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def divide(l,r):
            if l>=r:
                return 
            mid=(l+r)//2
            divide(l,mid)
            divide(mid+1,r)
            merge(l,mid,r)
        def merge(l,mid,r):
            n1=mid-l+1
            n2=r-mid
            lft=[0]*n1
            rgt=[0]*n2
            k=l
            for i in range(n1):
                lft[i]=nums[k]
                k+=1
            for j in range(n2):
                rgt[j]=nums[k]
                k+=1
            i=j=0
            k=l
            while(i<n1 and j<n2):
                if(lft[i]<rgt[j]):
                    nums[k]=lft[i]
                    i+=1
                else:
                    nums[k]=rgt[j]
                    j+=1
                k+=1
            while(i<n1):
                nums[k]=lft[i]
                i+=1
                k+=1
            while(j<n2):
                nums[k]=rgt[j]
                j+=1
                k+=1
            return nums
        l=0
        r=len(nums)-1
        divide(l,r)
        return nums