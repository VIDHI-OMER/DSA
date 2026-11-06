class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        l=[]
        st=set()
        def solve(lst):
            if len(lst)==n:
                l.append(lst[:])
                return
            for i in range(n):
                if i not in st:
                    if i>0 and nums[i]==nums[i-1] and i-1 not in st:
                        continue
                    st.add(i)
                    lst.append(nums[i])
                    solve(lst)
                    st.remove(i)
                    lst.pop()
        solve([])
        return l