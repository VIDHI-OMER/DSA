class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c=0
        st=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and i!=k and digits[i]!=0 and digits[k]%2==0:
                        num=digits[i]*100+digits[j]*10+digits[k]
                        st.add(num)
        return len(st)
                    
        