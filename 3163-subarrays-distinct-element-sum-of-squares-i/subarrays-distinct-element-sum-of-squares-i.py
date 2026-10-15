class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            st=set()
            for j in range(i,n):
                st.add(nums[j])
                s+=len(st)**2
        return s

        