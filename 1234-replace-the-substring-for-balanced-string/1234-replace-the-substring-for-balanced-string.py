class Solution:
    def balancedString(self, s: str) -> int:
        
        
        count = Counter(s)
        length = len(s) // 4
        left = 0
        right = 0
        ccs  = False
        
        for cc in count:
            if count[cc] != length:
                ccs= True
        
        result = len(s)
        
        if ccs:
            for right in range(len(s)):
                
                count[s[right]] -= 1
                
                ccs = False
                
                for cc in count:    
                    if count[cc] > length:
                        ccs= True
                
                while not ccs and left < right and count[s[left]] < length:
                    count[s[left]] += 1
                    left += 1
                
                if not ccs:
                    result = min(result, right - left + 1)
                
            return result
        
        else:
            return 0