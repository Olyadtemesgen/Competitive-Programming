class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            
            if p.val < root.val and root.val > q.val:
                root = root.left
            
            elif p.val > root.val and root.val < q.val:
                root = root.right
            
            else:
                return root