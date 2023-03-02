class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        prefix = 0
        
        prefix_in_hash = {0:1}
        answer = 0
        
        for right in range(len(nums)):
            prefix += nums[right]
            
            if prefix == goal:
                answer += prefix_in_hash[0]
                
            elif prefix - goal in prefix_in_hash:
                answer += prefix_in_hash[prefix- goal]
            
            prefix_in_hash[prefix] = prefix_in_hash.get(prefix, 0) + 1
        
        return answer