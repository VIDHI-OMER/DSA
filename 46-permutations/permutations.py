class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        st=set()
        l=[]
        def solve(lst):
            if len(lst)==len(nums):
                l.append(lst[:])
                return 
            for i in range(len(nums)):
                if i not in st:
                    lst.append(nums[i])
                    st.add(i)
                    solve(lst)
                    lst.pop()
                    st.remove(i)
        solve([])
        return l
            
        