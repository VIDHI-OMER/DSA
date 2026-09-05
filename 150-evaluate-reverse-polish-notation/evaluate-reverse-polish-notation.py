class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
        
            if i=='+':
                fst=int(st.pop())
                scnd=int(st.pop())
                st.append(scnd+fst)
            elif i=='-':
                fst=int(st.pop())
                scnd=int(st.pop())
                st.append(scnd-fst)
            elif i=='*':
                fst=int(st.pop())
                scnd=int(st.pop())
                st.append(scnd*fst)
            elif i=='/':
                fst=int(st.pop())
                scnd=int(st.pop())
                st.append(int(scnd/fst))
            else:
                st.append(i)
        return int(st[-1])

            
        