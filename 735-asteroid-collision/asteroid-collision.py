class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            while(st and i<0 and st[-1]>0):
                s=i+st[-1]
                if s<0:
                    st.pop()
                elif s>0:
                    i=0
                    break
                else:
                    st.pop()
                    i=0 
            if(i!=0):
                st.append(i)
        return st
            
        