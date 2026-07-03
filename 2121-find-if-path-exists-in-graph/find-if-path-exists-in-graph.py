class Solution:
    from collections import defaultdict
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g=defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i) 
        #print(g) 
        visited=set()
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for nei in g[node]:
                if dfs(nei):
                    return True
            return False

        return dfs(source)
