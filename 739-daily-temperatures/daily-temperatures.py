class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(temp)
        for t in range(len(temp)):
            while(st and st[-1][0]<temp[t]):
                tempp,idx=st.pop()
                ans[idx]=t-idx
            st.append([temp[t],t])
        return ans
        