# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        leftTree=self.lowestCommonAncestor(root.left,p,q)
        rightTree=self.lowestCommonAncestor(root.right,p,q)
        if leftTree and rightTree:
            return root
        return leftTree if leftTree else rightTree
        #dfs + preorder
        #10min thinking
        #my first thought of solving was same good

        
        
