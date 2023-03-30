class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
        answer = []
        
        def fn(array, res):
            
            nonlocal answer
            nonlocal length
            
            if len(res) == length:
                
                ans = res.copy()
                
                answer.append(ans)
                
                return

            for x in range(len(array)):
                fn(array[:x] + array[x + 1:], res + [array[x]])
        
        fn(nums, [])
        
        return answer
