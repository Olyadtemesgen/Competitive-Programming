class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        self.answer = 0
        demo = {}
        
        def brute_force(index, turn):
            
            if index >= len(prices):
                return 0
            
            if (index, turn) in demo:
                return demo[(index, turn)]
                
            if turn:
                 demo[(index, turn)] = max(brute_force(index + 1, False) - prices[index] - fee, brute_force(index + 1, turn))
            
            else:
                demo[(index, turn)] = max(brute_force(index + 1, True) + prices[index], brute_force(index + 1, turn))
            
            return demo[(index, turn)]
        
        return brute_force(0, True)
            