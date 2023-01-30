class Solution:
    def maxOperations(self, nums, k):
        
        nums.sort()
        
        result = 0
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            while nums[right] + nums[left] < k:    
                left += 1
                
            if left < right and nums[right] + nums[left] == k:
                result += 1
                left += 1
            
            right -= 1
        
        return result