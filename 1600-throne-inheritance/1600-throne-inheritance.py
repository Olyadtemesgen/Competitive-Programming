class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.result = []
        self.size = 0
        self.pc = defaultdict()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
        self.pc[childName] = parentName
        
    def death(self, name: str) -> None:
        # print(self.graph)
        if name == self.king:
            self.king = '5'
            value = self.graph[name]
            del self.graph[name]
            self.graph['5'] = value
            for x in value:
                self.pc[x] = '5'
        
        else:
            
            vvs = " " * self.size
            self.graph[self.pc[name]][self.graph[self.pc[name]].index(name)] = vvs
            
            value = self.graph[name]
            del self.graph[name]
        
            self.graph[vvs] = value
            for x in value:
                self.pc[x] = vvs
          
            
        self.size += 1
        
    def getInheritanceOrder(self) -> List[str]:
        
        result = []
        def dfs(king, visited):
            
            nonlocal result
            if king in visited:
                return
            
            if " " not in king and king and king != '5':
                result.append(king)
            
            visited.add(king)
            
            for kk in self.graph[king]:
                
                if kk not in visited:
                    dfs(kk, visited)
        
        dfs(self.king, set())
        
        return result
            

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()