class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        colors = [0] * len(graph)
        
        for x in range(len(graph)):
            
            # colors = [0] * len(graph)
            has_cycle = self.has_cycles(x, colors, graph)
            
            if not has_cycle:
                answer.append(x)
        
        return answer
    
    def has_cycles(self, current, colors, graph):
        if colors[current] == 1:
            return True
        
        if colors[current] == 2:
            return False
        
        colors[current] = 1
        
        for neighbour in graph[current]:
            
            if self.has_cycles(neighbour, colors, graph):
                return True

        colors[current] = 2
        
        return False