class Solution:
    def totalFruit(self, s: List[int]) -> int:
        
        counter = {}
        
        left = 0
        result = 0
        
        for right in range(len(s)):
            
            if s[right] not in counter:
                
                if len(counter) == 2:
                    
                    while counter[s[left]]:
                        counter[s[left]] -= 1
                        
                        if not counter[s[left]]:
                            del counter[s[left]]
                            break
                            
                        left += 1
                    
                    counter[s[right]] = 1
                    left += 1
                else:
                    counter[s[right]] = 1
            
            else:
                counter[s[right]] += 1
            
            result = max(right - left + 1, result)
        
        return result