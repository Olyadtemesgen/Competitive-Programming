class Solution:
    def maximumUniqueSubarray(self, s: List[int]) -> int:
        
        counter = {}
        result = 0
        left = 0
        right = 0
        summ = 0
        for right in range(len(s)):
            summ += s[right]
            
            if s[right] in counter:
                
                
                while s[left] != s[right]:
                    
                    del counter[s[left]]
                    summ -= s[left]
                    left += 1
                    
                summ -= s[left] 
                left += 1
                
            counter[s[right]] = 1
            
            result = max(result, summ)
                
        return result
                
                