class DesjointGraph:

    def __init__(self, size):
        self.parent = {i:i for i in range(1, size + 1)}

    def find_parent(self, child):

        while child != self.parent[child]:
            child = self.parent[child]
        
        return child
    
    def union(self,ch1, ch2):
        
        child1 = self.find_parent(ch1)
        child2 = self.find_parent(ch2)

        if child1 != child2:
            self.parent[child1] = child2
    
    def is_connected(self, a, b):
        return self.find_parent(a) == self.find_parent(b)


class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        res = []
        
        DS = DesjointGraph(
            len(edges))
        
        for f, t in edges:
            
            t_parent = DS.find_parent(t)
            f_parent = DS.find_parent(f)
            
            if t_parent == f_parent:
                res = [f, t]
                continue
            
            else:
                DS.union(f, t)
        
        return res