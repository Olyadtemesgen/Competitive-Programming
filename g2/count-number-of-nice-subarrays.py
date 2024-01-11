class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        result = 0
        summ = 0
        count = 0
        
        lll = left
        for right in range(len(nums)):
            
            summ += (nums[right] % 2)
            
            if summ == k:
                
                count = 0
                while left <= right and summ == k:

                    summ -= nums[left] % 2
                    count += 1
                    left += 1
            
            result += count
                
        return result
        ###############################