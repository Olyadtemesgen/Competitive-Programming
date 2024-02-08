class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        left = [1, nums[0]]
        right = [1, nums[-1]]
        length = len(nums)
        
        for rr in range(1, len(nums)):
            left.append(left[-1] * nums[rr])
            right.append(right[-1] * nums[length - rr - 1])
        
        right.reverse()
        
        for index in range(1, length + 1):
            nums[index - 1] = left[index - 1] * right[index]
        
        return nums