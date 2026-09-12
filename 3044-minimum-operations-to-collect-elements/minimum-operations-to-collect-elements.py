class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        st=set()
        for i in range(len(nums)-1,-1,-1):
            res+=1
            if nums[i]<=k:
                st.add(nums[i])
            if len(st)==k:
                return res