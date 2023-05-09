# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        answer = [root.val]
        while queue:

            for length in range(len(queue)):

                value = queue.popleft()
                
                if value.left:
                    queue.append(value.left)
                
                if value.right:
                    queue.append(value.right)
            
            vals = 0
            
            for qu in queue:
                vals += qu.val
            
            if queue:
                answer.append(vals / len(queue))
        
        return answer