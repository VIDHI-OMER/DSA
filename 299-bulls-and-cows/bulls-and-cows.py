class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        secret=list(secret)
        guess=list(guess)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                secret[i]='C'
                guess[i]='C'
        #print(bull,val)
        d={}
        for i in range(len(secret)):
            if secret[i]!='C':
                if secret[i] not in d:
                    d[secret[i]]=1
                else:
                    d[secret[i]]+=1
        for i in range(len(guess)):
            if guess[i]!='C':
                if guess[i] in d:
                    cow+=1
                    d[guess[i]]-=1
                    if d[guess[i]]==0:
                        del d[guess[i]]
        ans=f'{bull}A{cow}B'
        return ans
        
            

        