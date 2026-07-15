class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l2=[]
        for i in digits:
            if i in l:
                l2.append(l[i])
        print(l2)
        ans = []

        def dfs(index, path):
            if index==len(l2):
                ans.append(path)
                return
            for ch in l2[index]:
                dfs(index+1,path+ch)

        dfs(0, "")
        return ans