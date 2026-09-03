class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        mini=min(nums1)
        if mini%2==1:
            return True
        for i in range(len(nums1)):
            if nums1[i]%2==1:
                return False
        return True
            



        