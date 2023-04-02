class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        index = 0
        
        while index < len(nums):
            
            if nums[index] > len(nums) or nums[index] < 1 or nums[index] - 1 == index or nums[index] == nums[nums[index] - 1]:
                index += 1
            
            elif nums[index] != index + 1:
                saved_index = nums[index]
                nums[saved_index - 1], nums[index] = nums[index], nums[saved_index - 1]
            
            else:
                index += 1

        for index in range(len(nums)):
            
            if nums[index] - 1 != index:
                return index + 1
            
        return len(nums) + 1