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
                self.rank[parent1] += self.rank[parent2]
            
            elif self.rank[parent1] < self.rank[parent2]:
                self.parents[parent1] = parent2
                self.rank[parent2] += self.rank[parent1]
            
            else:
                self.parents[parent1] = parent2
                self.rank[parent2] += self.rank[parent1]
        
    
    def isConnected(self, node1, node2):
        return self.representative(node1) == self.representative(node2)
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        maxi1 = 0
        maxi2 = 0
        
        for stone in stones:
            maxi1 = max(stone[0], maxi1)
            maxi2 = max(stone[1], maxi2)
        
        ds = DisjointSet(maxi1 + maxi2 + 2)
        
        # all = len(stones)
        
        vstd = set()
        
        for row, col in stones:
            ds.union(row, col + maxi1 + 1)
            vstd.add(row)
            vstd.add(col + maxi1 + 1)
        
        not_connected = 0
        
        for ind in vstd:
            
            if ds.representative(ind) == ind:
                not_connected += 1

        return len(stones) - not_connected