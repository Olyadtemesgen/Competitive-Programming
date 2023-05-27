class Solution:
    
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        res = nums[0]
        
        lengt  = 2
        prev = nums[0]
        
        for x in range(1, len(nums)):
            
            prev += nums[x]
            res = max(res, math.ceil(prev / lengt))
            lengt += 1
        
        return res