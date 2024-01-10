class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        for left in range(len(nums)):
            if not nums[right] - val:
                while nums[right] == val  and right > left:
                    right -= 1
            if not nums[left] - val:
                nums[left], nums[right] = nums[right], nums[left]
            if left == right and nums[left] != val:return left + 1
            elif left == right:return left