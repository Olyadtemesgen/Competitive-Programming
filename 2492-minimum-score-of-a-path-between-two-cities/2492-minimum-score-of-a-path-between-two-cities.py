class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        DS = DisjointSet(1+n)
        
        for fr, to, cost in roads:
            DS.union(fr, to )
        
        minimum = inf
        
        for fr, to, cost in roads:
            
            if DS.isConnected(fr ,1):
                minimum = min(minimum, cost)
        
        return minimum
    
class DisjointSet:
    
    def __init__(self, n):
        
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def representative(self, node):
        
        if self.parents[node] == node:
            return node
        
        self.parents[node] = self.representative(self.parents[node])
        
        return self.parents[node]
    
    def union(self, node1, node2):
        
        parent1 = self.representative(node1)
        parent2 = self.representative(node2)
        
        if parent1 != parent2:
            
            if self.rank[parent1] > self.rank[parent2]:
                self.parents[parent2] = parent1
            
            elif self.rank[parent1] < self.rank[parent2]:
                self.parents[parent1] = parent2
            
            else:
                self.parents[parent1] = parent2
                self.rank[parent2] += 1
        
    
    def isConnected(self, node1, node2):
        return self.representative(node1) == self.representative(node2)