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
        left = count = nice_count = odd_count = 0
        
        for j in range(len(nums)):
            
            if nums[j] % 2:
                
                odd_count += 1
                
                if odd_count == k:
                    count = 0
                    
                    while odd_count == k:
                        
                        if nums[left] % 2:
                            odd_count -= 1
                        
                        left += 1
                        count += 1
            
            nice_count += count

        return nice_count