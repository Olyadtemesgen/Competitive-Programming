# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        
        left_arr = [[] for ii  in range(2002)]
        right_arr = []

        def go_through(root, right_a, depth):

            if not root:
                return
            
            right_a[depth].append(root.val)
            
            go_through(root.left,right_a, depth + 1)
            go_through(root.right, right_a, depth + 1)
            
            return
        
        go_through(root, left_arr, 0)
        result = []
        
        for index in left_arr:
            
            if index:
                result.append(index)
            
            else:
                break
        
        return result