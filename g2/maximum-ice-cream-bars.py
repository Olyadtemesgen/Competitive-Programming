class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()

        a = 0
        index = 0
        while a < coins and index < len(costs):
            a += costs[index]
            index += 1
        

        return index if a <= coins else index - 1
