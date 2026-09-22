class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        val=[]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                val.append(i)
                bull+=1
        #print(bull,val)
        d={}
        for i in range(len(secret)):
            if i not in val:
                if secret[i] not in d:
                    d[secret[i]]=1
                else:
                    d[secret[i]]+=1
        for i in range(len(guess)):
            if i not in val:
                if guess[i] in d:
                    cow+=1
                    d[guess[i]]-=1
                    if d[guess[i]]==0:
                        del d[guess[i]]
        ans=f'{bull}A{cow}B'
        return ans
        
            

        