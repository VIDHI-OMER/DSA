class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxi=0
        
        for i in range(len(nums)):
            odd=0
            even=0
            s=set()
            for j in range(i,len(nums)):
                if nums[j] not in s:
                    s.add(nums[j])
                    if nums[j]%2==0:
                        even+=1
                    else:
                        odd+=1
                if even==odd:
                    maxi=max(maxi,j-i+1)
        return maxi

