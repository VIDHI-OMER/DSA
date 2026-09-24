class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        i=j=0
        maxi=0
        while(i<n and j<m):
            if(nums1[i]>nums2[j]):
                i+=1
            maxi=max(maxi,j-i)
            j+=1
        return maxi

