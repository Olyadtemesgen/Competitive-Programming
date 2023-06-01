class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = defaultdict(lambda: inf)
        self.answer = inf
        
        def dp(amont):
            
            if amont in memo:
                return memo[amont] + 1
            
            if not amont:
                return 0
            
            elif amont < 0:
                return inf
            
            for amnt in coins:
                memo[amont] = min(memo[amont], dp(amont - amnt))
            
            return memo[amont] + 1
        
        val = dp(amount)
        
        return -1 if val == inf else val
    
            