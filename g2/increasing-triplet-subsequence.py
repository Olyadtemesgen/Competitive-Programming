class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        mi = -inf
        ma = inf
        md = inf
        
        for x in range(1, len(nums)):
            
            if mi != -inf:
                
                if nums[x] > md:
                    return True
                
                elif md > nums[x]:
                    
                    if nums[x] > mi:
                        md = nums[x]
                    
                    elif nums[x] < mi:
                        mi = nums[x]
            
            elif nums[x] > nums[x - 1]:
                
                mi = nums[x - 1]
                md = nums[x]
        
        return False
            