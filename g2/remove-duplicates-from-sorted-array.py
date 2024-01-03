class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        nums[:] = nums[:left + 1]