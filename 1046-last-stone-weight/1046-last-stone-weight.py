class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: -x, stones))
        
        heapq.heapify(stones)
        
        while stones:
            
            if len(stones) == 1:
                return -stones[0]
            
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            
            if val1 > val2:
                heapq.heappush(stones, val2 - val1)
            
            elif val2 > val1:
                heapq.heappush(stones, val1 - val2)
        
        return 0