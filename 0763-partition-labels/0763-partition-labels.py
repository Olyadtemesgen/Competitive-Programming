class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        left = 0
        right = 0
        result = []

        counter = Counter(s)
        array = []
        left = 0

        for right in range(len(s)):
            
            if s[right] not in array:
                counter[s[right]] -= 1
                
                if counter[s[right]] != 0:
                    array.append(s[right])
            
            else:
                counter[s[right]] -= 1
                
                if counter[s[right]] == 0:
                    array.pop(array.index(s[right]))
            
            if not array:
                result.append(right - left + 1)
                left = right + 1
        
        return result