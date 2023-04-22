class Solution:
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        
        answer = [0] * n
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        def dfs(graph, start,  array, parent):
            
            nonlocal answer
        
            glob = [0] * 26

            for x in graph[start]:
                
                if x != parent:
                    value = dfs(graph, x, array, start)
                    
                    for aa in range(26):
                        glob[aa] += value[aa]
                
                    
            
            answer[start] =  glob[ord(labels[start]) - 97] + 1

            glob[ord(labels[start]) - 97] += 1
            
            
            
            return glob
        
        
        dfs(graph, 0, [0] * 26, -1)
        
        return answer