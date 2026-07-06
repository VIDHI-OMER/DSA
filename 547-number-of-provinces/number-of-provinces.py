class Solution:
    from collections import defaultdict
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in range(len(isConnected)):
            for j  in range(len(isConnected)):
                if(isConnected[i][j]==1 and i!=j):
                    d[i].append(j)
        vis=set()
        
        def dfs(node):
            vis.add(node)
            for ngh in d[node]:
                if(ngh not in vis):
                    dfs(ngh)
        c=0       
        for i in range(len(isConnected)):
            if i not in vis:
                dfs(i)
                c+=1 
        return c          

        