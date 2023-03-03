
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        if not nums:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            
            else:
                left = mid + 1
                
        if nums[left] != target and left < len(nums) - 1:
            left += 1
        
        if nums[left] == target:
            
            left1 = left
            right1 = len(nums) - 1
            
            while left1 < right1:
                
                mid = (left1 + right1) // 2

                if nums[mid] > target:
                     right1 = mid - 1
                else:
                    left1 = mid + 1
               
            return [left, left1 if nums[left1] == target else left1 - 1]
        
        return [-1, -1]