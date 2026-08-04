class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        l=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                l.append(i)
        return l