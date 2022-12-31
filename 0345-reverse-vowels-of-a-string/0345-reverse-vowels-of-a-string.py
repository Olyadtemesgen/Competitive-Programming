class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        
        
        while left < right:
            
            while left < right and s[left] not in 'aeiouAEIOU':
                left += 1
            
            while left < right and s[right] not in 'aeiouAEIOU':
                right -= 1
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1
            
        return ''.join(s)