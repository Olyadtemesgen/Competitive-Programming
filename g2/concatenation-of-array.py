class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        for index in range(length):

            nums.append(nums[index])
        
        return nums