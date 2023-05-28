class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        minimum_until = defaultdict(int)

        for i in range(2, len(cost) + 1):
            minimum_until[i] = min(minimum_until[i - 1] + cost[i - 1], minimum_until[i - 2] + cost[i - 2])
        
        return minimum_until[len(cost)]