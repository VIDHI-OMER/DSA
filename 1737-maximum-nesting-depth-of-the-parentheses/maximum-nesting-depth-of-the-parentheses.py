class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        maxi=0
        for i in s:
            if i=='(':
                st.append('(')
                maxi=max(maxi,len(st))
            elif i==')':
                st.pop()
        return maxi
            
        