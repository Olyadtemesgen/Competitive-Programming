# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        result = defaultdict(int)
        maximum = 0
        
        def results(root):
            
            nonlocal result
            nonlocal maximum
            
            if not root:
                return
            
            result[root.val] += 1
            maximum = max(result[root.val], maximum)
            
            results(root.left)
            results(root.right)
        
        results(root)
        
        res = []
        for rr in result:
            if result[rr] == maximum:
                res.append(rr)
        
        return res