# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def dfs(root, parent):
            
            if not root:
                return
            if parent:
                graph[root.val].append(parent.val)
                
            if root.right:
                graph[root.val].append(root.right.val)
                dfs(root.right, root)
            
            if root.left:
                graph[root.val].append(root.left.val)
                dfs(root.left, root)
        
        dfs(root, None)
   
        queue = deque([])
        
        def bfs(root, visited, k):
          
            nonlocal queue
      
            queue.append(root)
            
            visited.add(root)
            
            while queue and k:
                
                for x in range(len(queue)):
                    
                    value = queue.popleft()
                    
                    for vals in graph[value]:
                        
                        if vals not in visited:
                            
                            visited.add(vals)
                            queue.append(vals)
                
                # print(queue)
                k -= 1
            
        bfs(target.val, set(), k)
        
        return list(queue)