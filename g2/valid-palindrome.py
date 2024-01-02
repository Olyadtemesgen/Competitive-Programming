class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s.strip()
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():left += 1
            while right > left and not s[right].isalnum():right -= 1
            if s[right] != s[left]:return False
            left += 1
            right -= 1
        return True