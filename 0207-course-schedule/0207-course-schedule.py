class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        graph2 = defaultdict(int)
        
        vv = set()
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            graph2[pre[0]] += 1
            
        
        queue = []
        
        for xx in range(numCourses):
            if not graph2[xx]:
                queue.append(xx)
        
        answer = []
        
        colors = [0] * numCourses
        
        for coot in queue:
            has_cycle = self.hascycle(coot, colors, graph, answer)
            
            if has_cycle:
                return []
        
        answer.reverse()
        
        if len(answer) != numCourses:
            return []

        return answer

        
    def hascycle(self, root, colors, graph, answer):
        if colors[root] == 2:
            return False

        if colors[root] == 1:
            return True

        colors[root] = 1

        for nei in graph[root]:
            iscycles = self.hascycle(nei, colors, graph, answer)

            if iscycles:
                return True

        colors[root] = 2

        answer.append(root)
        return False

    
