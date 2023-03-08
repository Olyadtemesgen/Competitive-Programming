# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symet(p, q):
            if not p and not q:
                return True

            if (not p and q) or (p and not q) or (p.val != q.val):
                return False

            return symet(p.left, q.right) and symet(p.right, q.left)
        
        return symet(root.left, root.right)