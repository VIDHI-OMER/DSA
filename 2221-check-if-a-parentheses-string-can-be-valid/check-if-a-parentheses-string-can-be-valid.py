class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        openn=[]
        opClo=[]
        if n%2==1:
            return False
        for i in range(n):
            if locked[i]=='0':
                opClo.append(i)
            elif s[i]=='(':
                openn.append(i)
            elif s[i]==')':
                if openn:
                    openn.pop()
                elif opClo:
                    opClo.pop()
                else:
                    return False
           
        #print(openn,opClo)
        while openn and opClo and openn[-1]<opClo[-1]:
            openn.pop()
            opClo.pop()
        return len(openn)==0