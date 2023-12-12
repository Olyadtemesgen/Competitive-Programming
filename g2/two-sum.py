class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums) - 1):
            
            if target - nums[x]- 1 + 1 in nums[x + 1:]:
                return [x, nums[x + 1:].index(target - nums[x]) + x + 1]