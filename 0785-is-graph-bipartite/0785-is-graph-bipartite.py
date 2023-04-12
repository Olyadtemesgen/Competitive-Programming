class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        graphs = {}
        index = 0
        
        for gr in graph:
            graphs[index] = gr
            index += 1

        answer = [-1 for x in range(len(graph))]
        
        value = True
        total = set()
        
        def dfs(node, color, visited):

            nonlocal value

            visited.add(node)
            answer[node] = color
            
            total.add(node)
            
            for neigh in graphs[node]:
                
                if answer[neigh] != -1 and color == answer[neigh] or not value:
                    value = False
                    return
                
                if neigh not in visited:
                    dfs(neigh, 1 - color, visited)
        
        for index in range(len(graph)):
            
            if not value:
                return False
            
            if index not in total:
                dfs(index, 1, set())
        
        return True