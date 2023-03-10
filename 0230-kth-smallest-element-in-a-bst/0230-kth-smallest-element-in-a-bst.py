# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def smallest(self, root, k):
        
        arr = []
        
        if not root:
            return []
        
        arr.extend(self.smallest(root.left, k))
        arr.extend([root.val])
        arr.extend(self.smallest(root.right,k))
        print(arr)
        return arr
    
    
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        val = self.smallest(root, k)
        
        return val[k - 1]