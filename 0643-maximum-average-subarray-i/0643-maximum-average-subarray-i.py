class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        right = k
        left = 0
        
        summ = sum(nums[:right])
        maximum = summ
        
        while right < len(nums):
            summ = summ - nums[left] + nums[right]
            
            left += 1
            right += 1
            
            maximum = max(summ, maximum)
            
        return maximum / k