class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maximum = [0] * len(prices)
        maximum[-1] = prices[-1]
        
        for index in range(len(prices) - 2, -1 , -1):
            maximum[index] = max(prices[index], maximum[index + 1])
        
        
        answer = 0
        minimum = prices[0]
        print(maximum)
        for index in range(1, len(prices)):
            
            answer = max(maximum[index] - minimum, answer)
            minimum = min(minimum, prices[index])
        
        return answer
    
            