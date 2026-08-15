class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n=len(tokens)
        i=0
        j=n-1
        c=0
        maxi=0
        tokens.sort()
        while(i<=j):
            if tokens[i]<=power:
                c+=1
                power-=tokens[i]
                i+=1
            elif c>=1:
                power+=tokens[j]
                c-=1
                j-=1
            else:
                break
            maxi=max(maxi,c)
        return maxi



        