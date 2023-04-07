class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        dicts = defaultdict(list)
        visited = set()
        
        for edge in edges:
            dicts[edge[0]].append(edge[1])
            dicts[edge[1]].append(edge[0])
        
        saved = False
        
        def dfs(dicts, source, visited):
            
            nonlocal saved
            
            if source == destination:
                saved = True
                return
            
            visited.add(source)
            
            for x in dicts[source]:
                
                if x not in visited:
                    dfs(dicts, x, visited)
                    
        
        dfs(dicts, source, visited)
        
        return saved