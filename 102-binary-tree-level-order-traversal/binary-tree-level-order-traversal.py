# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while q:
            new=[]
            depth=len(q)
            for i in range(depth):
                fst=q.popleft()
                new.append(fst.val)
                if fst.left:
                    q.append(fst.left)
                if fst.right:
                    q.append(fst.right)
            ans.append(new)
        return ans