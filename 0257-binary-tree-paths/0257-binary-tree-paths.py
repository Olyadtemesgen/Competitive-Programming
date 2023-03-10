# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        def binary_tree(root,  res):
            
            nonlocal result
            if not root:
                return
            
            if not root.right and not root.left:
                result.append(res + str(root.val))
                return
            
            binary_tree(root.left, res + str(root.val)+"->")
            binary_tree(root.right, res + str(root.val)+"->")
            
        
        binary_tree(root, "")
        return result