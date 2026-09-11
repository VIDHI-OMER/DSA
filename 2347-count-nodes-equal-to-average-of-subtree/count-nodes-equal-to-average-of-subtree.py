# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if root==None:
                return [0,0,0]
            p1=dfs(root.left)
            p2=dfs(root.right)
            tsum=p1[0]+p2[0]+root.val
            tc=p1[1]+p2[1]+1
            c=p1[2]+p2[2]
            avg=tsum//tc
            if avg==root.val:
                c+=1
            return [tsum,tc,c]
        return dfs(root)[2]