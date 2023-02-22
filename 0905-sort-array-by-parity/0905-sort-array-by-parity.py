class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0

        while right != left:

            while right != left and not nums[left] % 2:
                left += 1
            
            while right != left and nums[right] % 2:
                right -= 1
            
            nums[right], nums[left] = nums[left], nums[right]
        
        return nums
