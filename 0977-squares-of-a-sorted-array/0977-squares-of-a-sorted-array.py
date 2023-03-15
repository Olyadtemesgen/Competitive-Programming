class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for x in range(len(nums)):
            nums[x] **= 2
            
        return sorted(nums)