# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(TreeNode):
    
    def __init__(self):
        self.returned = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        left = []
        right = []
        
        
        if root.left:
            left = self.inorderTraversal(root.left)
        
        if root.right:
            right = self.inorderTraversal(root.right)
            
        res = left + [root.val] + right
        return res