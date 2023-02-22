class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        answer = []
        
        target = Counter(p)
        
        window = Counter(s[:len(p)])
        
        
        left = 0
        right = len(p)
        
        while right <= len(s):
            
            if target == window:
                answer.append(left)
            
            if right < len(s):
                window[s[left]] -= 1
                window[s[right]] = window.get(s[right], 0) + 1
            
            right += 1
            left += 1
        
        return answer