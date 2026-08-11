class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        s=0
        while(i<n-1 and nums[i]+1==nums[i+1]):
            s+=nums[i]
            i+=1
        s+=nums[i]
        st=set(nums)
        while(s in st):
            s+=1
        return s
        
