class Solution:
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = sum(nums) // threshold
        right = sum(nums)
        
        result = right
        
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            aa = 0
            if not mid:
                aa = 1
                mid += 1
            summ = 0
            
            for num in nums:
                summ += math.ceil(num / mid)
            
            if summ <= threshold:
                result = min(result, mid)
                right = mid - 1
            
            elif summ > threshold:
                left = mid + 1
            
            if mid == 1 and aa:
                break
        
        return result