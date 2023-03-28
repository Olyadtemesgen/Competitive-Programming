class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        left = 0
        
        counter = 0
        
        nums.append(-1)
        
        while left < len(nums):
            
            
            if nums[left] == len(nums):    
                nums[nums[left] - 1], nums[left] =  nums[left], nums[nums[left] - 1]
            
            else:
                nums[nums[left]], nums[left] = nums[left], nums[nums[left]]
            
            if nums[left] == left or nums[left] == -1:
                left += 1
            
            counter += 1
        
        return nums.index(-1)