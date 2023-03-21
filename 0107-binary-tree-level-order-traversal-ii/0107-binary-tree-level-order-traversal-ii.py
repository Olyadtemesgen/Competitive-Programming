# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = 0
        
        def max_depth(root, index):
            nonlocal answer
            
            if not root:
                return
            
            answer = max(answer, index)
            
            max_depth(root.left, index + 1)
            max_depth(root.right, index + 1)
        
        max_depth(root, 1)
        
        result = [[] for x in range(answer)]
        
        def result_finder(root, index):
            
            nonlocal result
            
            if not root:
                return
            
            result[len(result) - index - 1].append(root.val)
            
            result_finder(root.left, index + 1)
            
            result_finder(root.right, index + 1)
        
        
        result_finder(root, 0)
        
        return result