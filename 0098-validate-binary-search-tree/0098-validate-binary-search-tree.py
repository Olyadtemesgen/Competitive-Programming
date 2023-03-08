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
        
        stack = [(root, float("-inf"), float("inf"))]
        
        result = True
        while stack:
            
            root, left, right = stack.pop()
            if not root:
                continue

            if not (root.val > left and root.val < right):
                return False
            
            stack.append((root.left, left, root.val))
            stack.append((root.right, root.val, right))
        
        return result