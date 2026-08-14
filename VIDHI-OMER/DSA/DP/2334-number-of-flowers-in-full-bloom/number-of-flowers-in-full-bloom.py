class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n=len(people)
        def bsUpper(val,i,j):
            while(i<j):
                mid=(i+j)//2
                if(st[mid]<=val):
                    i=mid+1
                else:
                    j=mid
            return i
        
        def bsLower(val,i,j):
            while(i<j):
                mid=(i+j)//2
                if(ed[mid]>=val):
                    j=mid
                else:
                    i=mid+1
            return i
        st=[]
        ed=[]
        for i,j in flowers:
            st.append(i)
            ed.append(j)
        st.sort()
        ed.sort()
        m=len(st)
        ans=[]
        for d in people:
            upper=bsUpper(d,0,m)
            lower=bsLower(d,0,m)
            ans.append(upper-lower)
        return ans