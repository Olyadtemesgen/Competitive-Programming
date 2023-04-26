class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        
        for index in range(len(parent)):
            self.graph[parent[index]].append(index)
        
        self.locked = {}
        
    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:# and self.locked[num] != user:
            return False
        
        self.locked[num] = user
        return True
    
    def unlock(self, num: int, user: int) -> bool:
        if (num in self.locked and self.locked[num] != user) or num not in self.locked:
            return False
        
        if num in self.locked:
            del self.locked[num]
        
        return True
        
    def upgrade(self, num: int, user: int) -> bool:
        # print(self.locked)
        if num in self.locked:
            return False
        
        # visited = set()
        flag = False
        flag2 = False
        
        def dfs(start):
            
            nonlocal flag
            
            if start == 0:
                return
            
            if self.parent[start] in self.locked:
                flag = True
                return
            
            dfs(self.parent[start])
        
        dfs(num)
        
        value = set()
        
        if flag:
            # print('why not 2', (num, user))
            return False
        
        other_flag = False
        locked_ = set()
        
        def dfs2(start):
            
            nonlocal value
            value.add(start)
            
            nonlocal locked_
            
            if start in self.locked:
                locked_.add(start)
            
            for edge in self.graph[start]:
                dfs2(edge)
        
        dfs2(num)
        
        
        if not locked_:
            return False
        
        for nums in locked_:
            del self.locked[nums]
        
        self.locked[num] = user
        # print(self.locked)
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)