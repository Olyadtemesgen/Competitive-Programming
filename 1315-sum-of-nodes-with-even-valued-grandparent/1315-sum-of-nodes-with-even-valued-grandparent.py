# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        answer = 0
        def dfs(root, array):
            
            nonlocal answer
            
            if not root:
                return
            
            if len(array) < 2:
                array.append(root.val)
            
            elif not array[-2] % 2:
                answer += root.val
                array.append(root.val)
            
            else:
                array.append(root.val)
            # print(array)
            
            array2 = array.copy()
            dfs(root.left, array2)
            dfs(root.right, array)
        
        dfs(root, [])
        
        return answer