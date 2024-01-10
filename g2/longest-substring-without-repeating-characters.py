class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        counter = {}
        
        left = 0
        right = 0
        result = 0
        
        while right < len(s):
            
            if s[right] in counter:
                result = max(result, right - left)
                
                while s[left] != s[right]:
                    del counter[s[left]]
                    left += 1
                    
                left += 1
                counter[s[right]] = 1
                
            else:
                counter[s[right]] = 1
            
            right += 1
            
            result = max(result, right - left)
        return result