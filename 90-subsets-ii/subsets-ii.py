class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        st=set()
        def sub(i,l):
            if i>=len(nums):
                st.add(tuple(l))
                return
            l.append(nums[i])
            sub(i+1,l)
            l.pop()
            sub(i+1,l)
        sub(0,[])
        return sorted([list(x) for x in st])