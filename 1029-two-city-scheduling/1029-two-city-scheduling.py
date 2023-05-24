class Solution:
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        arr = []
        
        for i in range(len(costs)):
            arr.append([costs[i][0] - costs[i][1], i])
        
        arr.sort()
        
        answer = 0
        
        for x in range(len(costs)):
            if x < len(costs) // 2:
                answer += costs[arr[x][1]][0]
            
            else:
                answer += costs[arr[x][1]][1]
        
        return answer