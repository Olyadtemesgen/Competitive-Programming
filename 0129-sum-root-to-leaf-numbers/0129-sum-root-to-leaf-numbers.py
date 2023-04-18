# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(root, value):
            
            nonlocal total
            
            if not root:
                return
            
            if not root.left and not root.right:
                total += int(value + str(root.val))
                return
            
            value += str(root.val)
            
            dfs(root.left, value)
            dfs(root.right, value)
        
        dfs(root, "")
        
        return total