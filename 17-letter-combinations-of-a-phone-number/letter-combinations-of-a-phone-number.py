class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l2=[]
        for i in digits:
            if i in dic:
                l2.append(dic[i])
        ans=[]
        def dfs(i,lis):
            if i==len(l2):
                ans.append(lis)
                return
            for ch in l2[i]:
                dfs(i+1,lis+ch)
        dfs(0,'')
        return ans

        