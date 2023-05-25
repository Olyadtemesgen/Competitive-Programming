class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(set(nums)) <= 2:return False
        
        for index1 in range(len(nums) - 2):
            
            for y in range(index1 + 1, len(nums) - 1):
                
                if nums[index1] < nums[y] and max(nums[y + 1:]) > nums[y]:
                    return True
        
        return False