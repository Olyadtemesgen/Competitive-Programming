class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        
        for fro, to in edges:
            graph[to].append(fro)
        
        def dfs(root):
            
            is_visited.add(root)
            
            if result[root]:
                
                return result[root] + [root]
            
            answer = set()
            
            for roo in graph[root]:
                
                value =  dfs(roo)    

                answer = answer.union(set(value))

            result[root] = list(answer.copy())
            
            answer.add(root)      
            
            return answer
        
        result = defaultdict(list)
        
        
        colors = [0] * n
        
        is_visited = set()
        
        for index in range(n):

            if index not in is_visited:
                dfs(index)
            
        real_ans = []
        
        for vals in range(n):
            
            if not result[vals]:
                real_ans.append([])
            
            else:
                real_ans.append(sorted(result[vals]))
        
        return real_ans