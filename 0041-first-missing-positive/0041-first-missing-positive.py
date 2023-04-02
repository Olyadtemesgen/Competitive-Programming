class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        if 1 not in nums: return 1
        
        maximum = max(nums)
        
        if maximum < 1: return 1
        
        elif maximum == 1: return 2
        
        for x in range(2, maximum):
            
            if x not in nums:
                
                return x
        
        return maximum + 1