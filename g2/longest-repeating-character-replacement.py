class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, counter, maximum, result = 0, {}, 0, 0
        
        for right in range(len(s)):
            
            counter[s[right]] = counter.get(s[right], 0) + 1
            if maximum < counter[s[right]]:
                maximum = counter[s[right]] 
            while (right - left + 1) - maximum > k:
                counter[s[left]] -= 1
                left += 1
                
            result = max(result, right - left + 1)
            
        return result