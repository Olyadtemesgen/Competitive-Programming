class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        sums = sum(nums)

        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        for i in range(len(nums)):
            if not i or i == len(nums) - 1:
                if prefix[-1] - nums[i] == 0:
                    return i
            
            else:
                if prefix[i - 1] == prefix[-1] - prefix[i]:
                    return i
        
        return -1
                
            
                
