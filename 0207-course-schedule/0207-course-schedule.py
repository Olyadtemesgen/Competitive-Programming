class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        graph2 = defaultdict(int)
        
        vv = set()
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            graph2[pre[0]] += 1
            
        
        queue = deque([])
        
        for xx in range(numCourses):
            if not graph2[xx]:
                queue.append(xx)
        
        answer = []
        
        while queue:
            
            value = queue.popleft()
            
            answer.append(value)
            
            for x in graph[value]:
                
                graph2[x] -= 1
                
                if graph2[x] == 0:
                    queue.append(x)
        
        if len(answer) == numCourses:
            return True
        
        return False
            
            
                
                
