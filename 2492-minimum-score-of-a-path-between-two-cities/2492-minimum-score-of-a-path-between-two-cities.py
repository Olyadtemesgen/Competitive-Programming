class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        cost = defaultdict(lambda:float('inf'))
        for road in roads:
            
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
            cost[(road[0], road[1])] = road[2]
            cost[(road[1], road[0])] = road[2]
            
        
        minimum = float('inf')
        
        queue = deque()
        queue.append((1, -1))
        
        visited = set()
        while queue:
            
            
            cur, par = queue.popleft()
            
            visited.add(cur)
            
            minimum = min(minimum, cost[(cur, par)])
            
            for x in graph[cur]:
                
                if x not in visited:
                    
                    queue.append((x, cur))
            
        return minimum
        