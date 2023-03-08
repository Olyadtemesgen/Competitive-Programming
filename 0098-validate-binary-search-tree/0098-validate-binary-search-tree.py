# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = 0
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, minimum_left, maximum_right):
            
            if not root:
                return True            
           
            if (root.val >= maximum_right or root.val <= minimum_left):
                return False
            
            return isValid(root.right, root.val, maximum_right) and isValid(root.left, minimum_left, root.val)
        
        return isValid(root, float("-inf"), float("inf"))