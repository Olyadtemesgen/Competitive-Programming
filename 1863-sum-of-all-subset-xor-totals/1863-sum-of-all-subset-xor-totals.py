class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def result(res, index):
            
            if index == len(nums):
                return res           
            
            return result(res, index + 1) + result(res ^ nums[index], index + 1)
        
        return result(0, 0)