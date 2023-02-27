class Solution:
    def maximumUniqueSubarray(self, s: List[int]) -> int:
        
        counter = {}
        result = 0
        left = 0
        right = 0
        
        for right in range(len(s)):
            
            if s[right] in counter:
                
                
                while s[left] != s[right]:
                    
                    del counter[s[left]]
                    left += 1
                    
                left += 1
                
            counter[s[right]] = 1
            
            result = max(result, sum(s[left:right + 1]))
                
        return result
                
                