class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp={}
        for i in range(len(knowledge)):
            mp[knowledge[i][0]]=knowledge[i][1]
        #print(mp)
        i=0
        res=''
        temp=''
        openBr=False
        while(i<len(s)):
            if s[i]=='(':
                openBr=True
            elif s[i]==')':
                openBr=False
                if temp in mp:
                    res+=mp[temp]
                    
                else:
                    res+='?'
                temp=''
            elif openBr:
                temp+=s[i]
            else:
                res+=s[i]
            
            i+=1
        return res
                


        
        