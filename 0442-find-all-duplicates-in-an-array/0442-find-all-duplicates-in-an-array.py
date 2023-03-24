class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = set()
        right = 0
        
        while right < len(nums):
            
            if right + 1 != nums[right] and nums[nums[right] - 1] == nums[right]:
                result.add(nums[right])
                right += 1
            
            elif right + 1 == nums[right]:
                right += 1
            
            if right < len(nums):
                nums[nums[right] - 1], nums[right] = nums[right] , nums[nums[right] - 1]

        return result