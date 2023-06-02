class Solution:

    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        self.var = 0
        
        def dp(index):
            
            if index > len(nums) - 1:
                return 0
            
            elif index == len(nums) - 1:
                
                self.var = max(nums[index], self.var)
                
                return nums[index]
            
            if index in memo:
                return memo[index]
            
            memo[index] = max(nums[index] + dp(index + 2), dp(index + 1))
            
            self.var = max(memo[index], self.var)
            
            return memo[index]
        
        dp(0)
        return self.var
        
        