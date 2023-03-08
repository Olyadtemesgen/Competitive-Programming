# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        
        elif not root2:
            return root1
        
        def merger(root1, root2):
 
            # print((root1.val, root2.val))
            if not root2:
                return
            
            if not root1.left and not root1.right:
                root1.val += root2.val
                root1.left = root2.left
                root1.right = root2.right
                return

            elif not root1.left and root2.left:
                
                root1.val += root2.val
                root1.left = root2.left
                return self.mergeTrees(root1.right, root2.right)

            elif not root1.right and root2.right:
                
                root1.val += root2.val
                root1.right = root2.right
                return self.mergeTrees(root1.left, root2.left)
            
            else:
                root1.val += root2.val
                self.mergeTrees(root1.left, root2.left)   
                self.mergeTrees(root1.right, root2.right)

            
        merger(root1, root2)
        return root1