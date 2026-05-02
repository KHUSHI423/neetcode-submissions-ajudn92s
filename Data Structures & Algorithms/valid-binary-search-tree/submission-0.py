# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val=[]
        def valid(node):
            if not node:
                return None
            valid(node.left)
            val.append(node.val)
            valid(node.right)
        valid(root)
        for i in range(1,len(val)):
            if val[i]<val[i-1]:
                return False
        return True
        