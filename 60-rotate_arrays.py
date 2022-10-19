class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k %= len(nums)
        if k <= len(nums):
            temp = nums[:len(nums) - k]
            nums[:k] = nums[len(nums) - k: len(nums)]
            nums[k:] = temp
