from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        count1 = Counter(t)
        length = 0
        answer = len(s) + 1
        result = ""

        for right in range(len(s)):
            if s[right] in count1:
                count1[s[right]] -= 1

            if s[right] in count1 and not  count1[s[right]]:
                length += 1
            
            if length == len(count1):

                while left < right and (s[left] not in count1 or count1[s[left]] < 0):
                    if count1[s[left]] < 0:
                        count1[s[left]] += 1

                    left += 1
                
                if answer >  right - left + 1:
                    # consistency
                    result = s[left:right + 1]
                    answer = right - left + 1
                
                count1[s[left]] += 1
                # accepted
                left += 1
                length -= 1
        
        return result