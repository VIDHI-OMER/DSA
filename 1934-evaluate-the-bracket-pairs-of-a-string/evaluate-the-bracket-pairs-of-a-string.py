class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp={}
        for i in range(len(knowledge)):
            mp[knowledge[i][0]]=knowledge[i][1]
        #print(mp)
        i=0
        res=''
        while(i<len(s)):
            if (s[i].isalpha()):
                res+=s[i]
            elif(s[i]=='('):
                i+=1
                temp=""
                while(s[i]!=')'):
                    temp+=s[i]
                    i+=1
                if temp in mp:
                    res+=mp[temp]
                else:
                    res+='?'
            i+=1
        return res
                


        
        