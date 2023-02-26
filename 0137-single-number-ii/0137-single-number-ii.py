class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        prev = 0
        curr = 1
        next = 2
        
        while next < len(nums):
            
            if nums[prev] != nums[curr] and nums[curr] == nums[next]:
                return nums[prev]
            
            prev += 3
            curr += 3
            next += 3
        
        return nums[-1]