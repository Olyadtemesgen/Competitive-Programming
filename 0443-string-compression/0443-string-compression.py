class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left, right= 0, 0
        
        while left < len(chars):
            
            if right < len(chars) and chars[right] == chars[left]:
                right += 1
            
            else:
                if right - left > 1:
                    
                    chars[left:right] = [chars[left]] + [a for a in str(right - left)]
                    left += len( [chars[left]] + [a for a in str(right - left)])
                    right = left
                
                else:
                    left = right
        
        return len(chars)