from collections import defaultdict,deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)
        vis=set()
        f=0
        def dfs(node):  
            vis.add(node)
            c=1
            ed=len(adj[node])
            for i in adj[node]:
                if i not in vis:
                    n,e=dfs(i)
                    c+=n
                    ed+=e
            return (c,ed)

        for i in range(n):
            if i not in vis:
                c,ed=dfs(i)
                ed//=2
                if(ed==c*(c-1)//2):
                    f+=1
        return f