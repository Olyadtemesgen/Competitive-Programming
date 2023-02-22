class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        dictionary = defaultdict(int)
        
        for right in range(len(nums)):
            
            if dictionary[nums[right]]:
                return True
            else:
                dictionary[nums[right]] += 1
                
            if right - left == k:
                dictionary[nums[left]] -= 1
                left += 1