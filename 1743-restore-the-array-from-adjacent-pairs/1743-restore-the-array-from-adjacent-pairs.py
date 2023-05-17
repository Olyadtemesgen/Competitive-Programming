class Solution:
    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for fr, to in adjacentPairs:
            graph[fr].append(to)
            graph[to].append(fr)
        
        self.answer = []
        def dfs(root, parent):
            
            
            
            
            for nei in graph[root]:
                
                if nei != parent:
                    self.answer.append(nei)
                    dfs(nei, root)
                    
    
        
        for xx in graph:
            
            if len(graph[xx]) == 1:    
                self.answer = [xx]
                dfs(xx, -1)
                return self.answer