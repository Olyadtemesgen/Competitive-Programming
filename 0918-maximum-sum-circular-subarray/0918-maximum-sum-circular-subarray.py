class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        minimum = nums[0]
        
        currentmax = 0
        currentmin = 0
        prefixsum = 0
        
        for num in nums:
            
            currentmax = max(currentmax + num,  num)
            currentmin = min(currentmin + num,  num)
            
            prefixsum += num
            
            maximum = max(maximum, currentmax)
            minimum = min(minimum, currentmin)
    
        if maximum > 0:
            return max(maximum, prefixsum - minimum)

        return maximum
        