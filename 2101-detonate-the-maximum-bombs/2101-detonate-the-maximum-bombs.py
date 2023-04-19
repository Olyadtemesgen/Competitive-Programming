class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        
        for root1 in range(len(bombs)):
            for root2 in range(len(bombs)):
                
                if root1 != root2 and (bombs[root1][0] - bombs[root2][0]) ** 2 + (bombs[root1][1] - bombs[root2][1]) ** 2 <= bombs[root1][2] ** 2:
                    graph[root1].add(root2)
                
                if  root1 != root2 and (bombs[root1][0] - bombs[root2][0]) ** 2 + (bombs[root1][1] - bombs[root2][1]) ** 2 <=(bombs[root2][2])**2:
                    graph[root2].add(root1)
        
    
        for count in graph:
            graph[count] = list(graph[count])

        maximum = 1
        
        def dfs(start, maxis, visited):
            
            # print(maxis)
            
            nonlocal maximum
            
            if start in visited:
                return
            
            visited.add(start)
            
            # maximum = max(maxis, maximum)
            
            for vals  in graph[start]:
                
                if vals not in visited:
      
                    value = maxis + 1
                   
                    dfs(vals, value, visited)
            
            maximum = max(len(visited), maximum)
            
            
        for val in range(len(bombs)):
            dfs(val, 1, set())
        
        return maximum