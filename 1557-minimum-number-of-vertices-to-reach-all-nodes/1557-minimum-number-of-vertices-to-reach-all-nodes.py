class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        answer = []
        
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[1]].append(edge[0])
        
        for x in range(n):
            if x not in graph:
                answer.append(x)
        
        return answer