from collections import deque


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        queue = deque([])
        result = [-1] * len(nums)

        length = len(nums)
        nums = nums + nums
        for right in range(len(nums)):
            
            rights = right % length

            while stack and nums[right] > nums[stack[-1]]:
                result[stack.pop()] = nums[right]
            
            if not stack or stack[-1] != rights:
                stack.append(rights)
        
      
        return result
