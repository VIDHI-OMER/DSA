class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        openn=0
        close=0
        maxi=0
        #left->right
        for i in s:
            if i=='(':
                openn+=1
            else:
                close+=1
            if (openn==close):
                maxi=max(openn+close,maxi)
            elif close>openn:
                openn=0
                close=0
        #right->left
        openn=0
        close=0
        for i in range(n-1,-1,-1):
            if s[i]==')':
                close+=1
            else:    
                openn+=1
            if (openn==close):
                maxi=max(openn+close,maxi)
            elif openn>close:
                openn=0
                close=0 
        return maxi