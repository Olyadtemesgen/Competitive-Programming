class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        lengths = Counter(s1)
        left = 0
        length = lengths
        counter = Counter(s2[:len(s1)])
        right = len(s1)
        
        while right < len(s2):
            
            if counter == length:
                return True
            
            counter[s2[left]] -= 1
            counter[s2[right]] += 1
            
            right += 1
            left += 1
        
        if counter == length:
            return True
        
        return False