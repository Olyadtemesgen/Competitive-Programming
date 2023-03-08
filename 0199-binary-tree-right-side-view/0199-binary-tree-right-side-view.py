# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = defaultdict(list)
        def rights(root, left, right):
            
            nonlocal result
            if not root:
                return

            result[left] = root.val
            
            rights(root.left, left + 1, right - 1)
            rights(root.right, left +1, right + 1)
        
        rights(root, 0, 0)
        res = []
        for xx in result:
            res.append(result[xx])
        
        return res