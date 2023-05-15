class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        graph2 = defaultdict(int)
        
        vv = set()
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            graph2[pre[0]] += 1
            
        
        stack = []
        
        for xx in range(numCourses):
            if not graph2[xx]:
                stack.append(xx)
        
        answer = []
        
        colors = [0] * numCourses
        
        top_to_ans = []
        
        for vals in range(numCourses):
            has_cycle = self.has_cycle(vals, colors, graph, top_to_ans)
            
            if has_cycle:
                return []
        
        top_to_ans.reverse()
        
        return top_to_ans
    
    def has_cycle(self, current, colors, graph, top_to_ans):
        if colors[current] == 1:
            return True
        
        elif colors[current] == 2:
            return False
        
        colors[current] = 1
        
        for neighbours in graph[current]:

            value = self.has_cycle(neighbours, colors, graph, top_to_ans)
        
            if value:
                return True
            
        top_to_ans.append(current)
        colors[current] = 2
        
        return False