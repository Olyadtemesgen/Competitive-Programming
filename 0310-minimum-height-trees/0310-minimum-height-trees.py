class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        counter = [0] * n
        
        for fr, to in edges:
            
            graph[fr].append(to)
            graph[to].append(fr)
            
            counter[fr] += 1
            counter[to] += 1
            
        todo = deque()
        visited = set()
        
        for node in graph:
            
            if len(graph[node]) == 1:
                todo.append(node)
                counter[node] -= 1
        
        visited = set(todo)
        ans = []

        while todo:
            
            if len(todo) <= 2:
                
                ans = todo.copy()
                
            for td in range(len(todo)):
                
                tdv = todo.popleft()
                
                for node in graph[tdv]:
                    
                    counter[node] -= 1
                    
                    if node not in visited and counter[node] == 1:

                        visited.add(node)
                        todo.append(node)
                
        return ans if ans else [0]