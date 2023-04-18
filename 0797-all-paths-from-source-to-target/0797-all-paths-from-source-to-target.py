class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []

        def dfs(start, answer):
           
            nonlocal result
            if start == len(graph) - 1:
                result.append(answer)
                # answer.pop()
                return
            
            for node in graph[start]:
                answer2 = answer.copy()
                answer2.append(node)
                dfs(node, answer2)
        
        dfs(0, [0])
        return result
        