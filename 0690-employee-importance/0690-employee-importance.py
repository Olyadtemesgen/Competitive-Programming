"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        importance = {}
        
        graph = {}
        
        for employee in employees:

            graph[employee.id] = employee.subordinates
            importance[employee.id] = employee.importance
        
        answer = 0
        
        def dfs(id):
            nonlocal answer
            
            answer += importance[id]
            
            for subordinate in graph[id]:
                dfs(subordinate)
        
        dfs(id)
        
        return answer