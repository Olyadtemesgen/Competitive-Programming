"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        answer = 0
        def dfs(root, depth):
            
            nonlocal answer
            
            if not root:
                return
            
            answer = max(answer, depth + 1)
            
            for child in root.children:
                dfs(child, depth + 1)
        
        dfs(root, 0)
        
        return answer