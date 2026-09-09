class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        st=[]
        j=0
        i=0
        for i in range(n):
            st.append(pushed[i])
            while st and j<n and st[-1]==popped[j]:
                st.pop()
                j+=1
        return len(st)==0

        