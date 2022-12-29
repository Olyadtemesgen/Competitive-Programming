class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        summ = 0

        for y in nums:  
            if not y % 2:
                summ += y

        for x in queries:
        
            if not nums[x[1]] % 2:
                summ -= nums[x[1]]
        
            nums[x[1]] = nums[x[1]] + x[0]
            
            if not nums[x[1]] % 2:
                summ += nums[x[1]]
            
            result.append(summ)
        
        return result