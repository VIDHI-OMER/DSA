class Solution:
    def isHappy(self, n: int) -> bool:
        st=set()
        while n!=1:
            if n in st:
                return False
            st.add(n)
            s=0
            while n>0:
                rem=n%10
                s+=rem**2
                n//=10
            n=s
        return True