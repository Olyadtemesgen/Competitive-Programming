class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        length = len(set(nums))


        left = 0

        counter = {}
        answer = 0

        for right in range(len(nums)):
            if nums[right] not in counter:
                counter[nums[right]] = 1
            
            else:
                counter[nums[right]] += 1
            
            if len(counter) == length:
                answer += 1
            
            while left < right and len(counter) == length:
                counter[nums[left]] -= 1
                
                if not counter[nums[left]]:
                    counter[nums[left]] += 1
                    break
                
                left += 1
            
            if len(counter) == length:
                answer += left
        
        return answer
                