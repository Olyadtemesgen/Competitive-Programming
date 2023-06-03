# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        demo = {}
        self.mas = 0
        def dp(root):
            
            if not root:
                
                return 0
            
            if not root.left and not root.right:
                self.mas = max(self.mas, root.val)
                return root.val
            
            if root in demo:
                
                return demo[root]
            
            if root.left and root.right:    
                demo[root] = max( dp(root.left) + dp(root.right), root.val + dp(root.left.left) + dp(root.right.right) + dp(root.left.right)+ dp(root.right.left))
            
            elif root.left:
                demo[root] = max(dp(root.left) + dp(root.right), root.val + dp(root.left.left) + dp(root.left.right))
            
            elif root.right:
                demo[root] = max( dp(root.left) + dp(root.right), root.val + dp(root.right.left) + dp(root.right.right))
            
            self.mas = max(self.mas, demo[root])
            return demo[root]
        
        dp(root)
        
        return self.mas
        
        