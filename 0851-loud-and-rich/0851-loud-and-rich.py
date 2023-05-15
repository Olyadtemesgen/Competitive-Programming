class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        
        for rich, poor in richer:
            graph[poor].append(rich)
        
        def dfs(root):
            
            if result[root] != -1:
                return result[root]
            
            is_visited.add(root)
            
            minimum = (float('inf'), -1)
            
            for nei in graph[root]:    
                value = dfs(nei)
                minimum = min(minimum, value)
            
            if minimum == (float('inf'), -1):
                result[root] = (quiet[root], root)
                return (quiet[root], root)
            
            else:
                result[root] = min(minimum, (quiet[root], root))
                
                return minimum
        
        
        is_visited = set()
        
        result = defaultdict(lambda:-1)
        
        for val in range(len(quiet)):
            # print(is_visited)
            if val not in is_visited:
                dfs(val)
        
            # print(result)
        
        answer2 = []
        
        for res in result:
            answer2.append(result[res][1])
        
        return answer2