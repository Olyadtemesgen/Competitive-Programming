class Solution:
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        subarray_sum = {0:1}
        result = 0
        sums = 0
        
        for num in nums:
            
            sums += num
            
            if sums - k in subarray_sum:
                result += subarray_sum[sums - k]
            
            subarray_sum[sums] = subarray_sum.get(sums, 0) +  1
    
        return result