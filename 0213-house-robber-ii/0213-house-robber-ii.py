class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        self.var = 0
        
        if len(nums) == 1:
            return nums[0]
        
        def dp(start, final):
            
            if start > final:
                return 0
            
            elif start == final:
                self.var = max(nums[start], self.var)
                return nums[start]
            
            if start in memo:
                
                return memo[start]
            
            memo[start] = max(nums[start] + dp(start + 2, final), dp(start + 1, final))
            
            self.var = max(memo[start], self.var)
            
            return memo[start]
                
        dp(0, len(nums) - 2)
        memo = {}
        dp(1, len(nums) - 1)
        
        return self.var