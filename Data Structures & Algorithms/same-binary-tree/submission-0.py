# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self,p,q):
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        if p.val!=q.val:
            return False
        l=self.sameTree(p.left,q.left)
        r=self.sameTree(p.right,q.right)
        return l and r
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.sameTree(p,q)
        
        
        