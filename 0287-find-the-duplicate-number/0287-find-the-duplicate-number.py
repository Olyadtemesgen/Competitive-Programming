class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]
        
        fast = nums[nums[fast]]
        slow = nums[slow]
        
        while slow != fast:
            
            fast = nums[nums[fast]]
            slow = nums[slow]
            
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow