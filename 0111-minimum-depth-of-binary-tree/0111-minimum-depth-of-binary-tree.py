# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        res = float("inf")
        
        if not root:
            return 0
    
        def minimum(root, result):
            
            nonlocal res
            
            if not root:
                return
            
            if not root.left and not root.right:    
                res = min(res, result)
                return 
            
            else:
                minimum(root.left, result + 1)
                minimum(root.right, result + 1)
        
        minimum(root, 0)
        return res + 1