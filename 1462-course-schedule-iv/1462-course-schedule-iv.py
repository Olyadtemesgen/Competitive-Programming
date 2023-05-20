class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        incoming  = [0] * numCourses
        
        for to, fr in prerequisites:
            graph[to].append(fr)
            incoming[fr] += 1
        
        todo = []
        
        for index in range(numCourses):
            if not incoming[index]:
                todo.append(index)
            
        colors = [0] * numCourses
        pre_each = defaultdict(set)
        
        
        
        def dfs(tod, colors, pre_each, vstd):
            

            if colors[tod] == 2:
                return {tod}.union(pre_each[tod])
            
            colors[tod] = 1
            
            value = set()
            
            for nodes in graph[tod]:
                
                result = dfs(nodes, colors, pre_each, vstd)
                
                value = value.union(result)
                
            pre_each[tod] = value.copy()
            colors[tod] = 2
            value.add(tod)
            
            return value
        
        for tod in todo:
            
            # visited = set()
            dfs(tod, colors, pre_each, set())
            
        answer = []
        
        for a, b in queries:
            answer.append(b in pre_each[a])
            
        # print(pre_each, incoming)
        return answer