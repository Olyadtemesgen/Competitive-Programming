class Solution:
    def __init__(self):
        self.visited = set()  
        
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graphs = {}
        for x in range(1, n + 1):
            graphs[x] = []
        
        for one, two in dislikes:
            graphs[one].append(two)
            graphs[two].append(one)
            
        answer = [-1 for x in range(n + 1)]
        
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
        
        for index in range(1, n + 1):
            
            if not value:
                return False
            
            if index not in total:
                dfs(index, 1, set())
        
        return True