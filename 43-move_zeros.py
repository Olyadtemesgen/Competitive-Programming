class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for x in nums:
            if x != 0:
                nums[counter] = x
                counter += 1
        if counter != len(nums):
            while counter != len(nums):
                nums[counter] = 0
                counter += 1
