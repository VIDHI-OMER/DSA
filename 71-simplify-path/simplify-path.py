class Solution:
    def simplifyPath(self, path: str) -> str:
        d=path.split('/')
        print(d)
        st=[]
        for i in d:
            if i=='' or i=='.':
                continue
            if i=='..':
                if st:
                    st.pop()
            else:
                st.append(i)
        if len(st)==0:
            return "/"
        return "/" + "/".join(st)
        