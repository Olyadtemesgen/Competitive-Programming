class Solution:
    def __init__(self):
        self.visited = set()
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        answer = 0
        
        graph = {}
        for index in range(1, len(isConnected) + 1):
            graph[index] = []
        
        for edge in range(len(isConnected)):
        
            for x in range(len(isConnected)):
                
                if isConnected[edge][x] and edge != x:
                    graph[edge + 1].append(x + 1)

        def dfs(node, graph, isvisited):
            
            self.visited.add(node)
            
            if not graph[node]:
                return
            
            if node in isvisited:
                return
            
            isvisited.add(node)
            
            
            
            for edg in graph[node]:
                
                if edg not in isvisited:
                        
                    dfs(edg, graph,isvisited)
        
        for edge in graph:
        
            isvisited = set()
            
            if edge not in self.visited:
                
                answer += 1
                dfs(edge, graph, set())
        
        return answer
        
   