class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for i in s:
            if i=='(':
                st.append(0)
            else:
                d=st.pop()
                if d==0:
                    score=1
                else:
                    score=2*d
                st[-1]+=score
        return st[0]