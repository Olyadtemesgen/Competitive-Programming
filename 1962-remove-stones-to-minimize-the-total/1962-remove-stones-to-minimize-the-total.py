class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = list(map(lambda x:-x, piles))
        heapq.heapify(piles)
        
        while k:
            
            value = -heapq.heappop(piles)
            
            if value:
                heapq.heappush(piles, value // 2 - value)
                k -= 1
                
        
        return -sum(piles)