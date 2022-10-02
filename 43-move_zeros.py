class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
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
    #by using two pointer we can solve it in such a way
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1
        while right < len(nums) and left < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                right += 1
                left += 1 
#commiyrd
