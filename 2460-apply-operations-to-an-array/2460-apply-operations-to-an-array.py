class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1):
            
            if nums[index] == nums[index + 1]:
                
                nums[index] *= 2
                nums[index + 1] = 0
            
        writer = 0
        reader = 0
        
        while reader < len(nums):
            
            if nums[reader] != 0:
                
                nums[writer], nums[reader] = nums[reader], nums[writer]
                
                writer += 1
            
            reader += 1
        
        return nums