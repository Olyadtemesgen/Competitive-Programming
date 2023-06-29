class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        demo = {}
        
        def brute_force(index, turn, num):
            
            if index >= len(prices) or num > 1:
                return 0
            
            if (index, turn, num - 1) in demo:
                return demo[(index, turn, num - 1)]
            
            elif (index, turn, num) in demo:
                return demo[(index, turn, num)]
            
            if turn:
                 demo[(index, turn, num)] = max(brute_force(index + 1, False, num) - prices[index], brute_force(index + 1, turn, num))
            
            else:
                demo[(index, turn, num)] = max(brute_force(index + 1, True, num + 1) + prices[index], brute_force(index + 1, turn, num))
            
            return demo[(index, turn, num)]
        
        return brute_force(0, True, 0)
            