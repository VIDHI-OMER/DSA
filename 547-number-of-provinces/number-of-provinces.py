class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c=0
        visited=set()
        def dfs(node):
            visited.add(node)
            for nei in range(len(isConnected)):
                if(isConnected[node][nei]==1 and nei not in visited):
                    dfs(nei)
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                c+=1
        return c

        