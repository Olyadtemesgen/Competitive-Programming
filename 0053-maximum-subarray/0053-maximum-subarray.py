class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        left = 0
        
        maximum = nums[0]
        for right in range(1, len(nums)):    
            
            maximum = max(maximum, result)
            
            if result < 0:
                
                while left < right:
                    result -= nums[left]
                    left += 1
                    
            
            result += nums[right]
            maximum = max(maximum, result)
                    
        return maximum