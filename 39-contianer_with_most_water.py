class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max = min(height[0], height[right]) * right
        while left != right:
            if min(height[left], height[right]) * (right - left) > max:
                max = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            elif  height[left + 1] > height[right - 1]:
                left += 1
            else:
                right -= 1
        return max
