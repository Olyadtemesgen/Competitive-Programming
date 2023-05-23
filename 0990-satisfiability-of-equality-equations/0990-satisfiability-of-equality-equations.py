class DisjointSet:
    def __init__(self):
        
        self.parent = [chr(x) for x in range(97, 123)]
        self.rank = [1 for _ in range(26)]
        
    def find(self,eq, ch1):
        
     
        if ch1 == self.parent[ord(ch1) - 97]:
            return ch1
        
        self.parent[ord(ch1) - 97] = self.find(eq, self.parent[ord(ch1) - 97])

        return self.parent[ord(ch1) - 97]
        
    def union(self,eq, ch1, ch2):
            
        ch1 = self.find(eq, ch1)
        ch2 = self.find(eq, ch2)
        
        if ch1 != ch2:
            if eq:
                
                if self.rank[ord(ch1) - 97] > self.rank[ord(ch2) - 97]:
                    self.parent[(ord(ch1)) - 97] = ch2

                elif self.rank[ord(ch1) - 97] < self.rank[ord(ch2) - 97]:
                    self.parent[(ord(ch2)) - 97] = ch1

                else:
                    self.parent[(ord(ch2)) - 97] = ch1
                    self.rank[(ord(ch1)) - 97] += 1
                

    def is_connected(self,eq, ch1, ch2):
        return self.find(eq, ch1) == self.find(eq, ch2)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        df = DisjointSet()
        
        
        for bef, eq, equal, aft in equations:
            
            if bef == aft and eq == "!":
                return False
            
            if eq == "=":
                
                df.union(True, bef, aft)
        
        for bef, eq, equal, aft in equations:
            
            if eq == "!":
                
                if df.is_connected(True, bef, aft):
                    return False
        
        return True