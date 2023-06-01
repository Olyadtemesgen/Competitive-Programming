class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dict = {}
        
        def dp(index, arr):
            
            
            if index == len(nums):  
                if arr == target:
                    return 1
                
                return 0
            
            if (index, arr) in dict:
                return dict[(index, arr)]
            
            dict[(index, arr)] = dp(index + 1, arr + nums[index]) + dp(index + 1, arr - nums[index])
            
            return dict[(index, arr)]

        
        return dp(0, 0)