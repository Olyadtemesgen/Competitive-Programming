# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        r_left = root.left
        r_right = root.right
        
        stack = [(root.left, root.right)]
        
        result = True
        
        while stack:
            left, right = stack.pop()
            
            if not right and not left:
                continue
            
            if (not right and left) or (right and not left) or (right.val != left.val):
                return False
            
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return result