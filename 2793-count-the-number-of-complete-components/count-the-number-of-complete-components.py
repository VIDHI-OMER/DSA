from collections import defaultdict,deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        print(adj)
        vis=set()
        req=n*(n-1)//2
        f=0
        for i in range(n):
            if i not in vis:
                q=deque()
                q.append(i)
                vis.add(i)
                c=0
                no_no=0
                while q:
                    d=q.popleft()
                    c+=1
                    no_no+= len(adj[d])
                    for neg in adj[d]:
                        if neg not in vis:
                            vis.add(neg)
                            q.append(neg)
                no_no=no_no//2
                req = c*(c - 1)//2
                if(no_no==req):
                    f+=1
        return f
                        
                
                


            