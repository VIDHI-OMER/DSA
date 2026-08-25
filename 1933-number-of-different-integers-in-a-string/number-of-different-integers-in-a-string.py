class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        c=''
        ans=[]
        for i in word:
            if i.isdigit():
                c+=i
            else:
                ans.append(c)
                c=''
        if c:
            ans.append(c)
        st=set()
        for i in ans:
            if i:
                i=int(i)
                if i not in st:
                    st.add(i)
        return len(st)
        
