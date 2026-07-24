class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        st=set()
        st2=set()
        
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                st.add(nums[i]^nums[j])
        print(st)
        lst=list(st)
        for i in range(n):
            for j in range(len(lst)):
                st2.add(nums[i]^lst[j])
        return len(st2)
            