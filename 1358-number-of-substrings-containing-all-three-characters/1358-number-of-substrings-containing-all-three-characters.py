class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = 0
        counter = defaultdict(int)
        count = 0
        result = 0
        
        for right in range(len(s)):
            counter[s[right]] += 1
            
                
            if len(counter) == 3:

                while len(counter) == 3:

                    counter[s[left]] -= 1

                    if not counter[s[left]]:
                        del counter[s[left]]

                    left += 1
                    count += 1
                        
            
            result += count
        
        return result
    