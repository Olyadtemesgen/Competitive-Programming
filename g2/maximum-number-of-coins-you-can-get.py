class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        
        length = len(piles) // 3
        
        lens = len(piles) - 2
        answer = 0

        while length:
            
            answer += piles[lens]
            
            lens -= 2
            length -= 1
        return answer