class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:    
        num = 0

        index = 0
        i = 0

        while  i < len(nums) - 1:
            if (nums[i] > nums[i + 1]):
                if not i:
                    num += 1
                
                else:
                    if num:
                        return False
                    
                    if nums[i - 1] > nums[i + 1] and i + 2 < len(nums) and nums[i] > nums[i + 2]:
                        return False
                    
                    num += 1
            
            i += 1
        
        return True