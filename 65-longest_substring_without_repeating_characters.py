class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 1
        l = 0
        summ = 0
        if len(s) <= 2:
            return len(set(s))
        while r < len(s) - 1:
            if s[r] not in s[l:r]:
                summ = max(summ, r - l + 1)
                r += 1
            elif s[r] in s[l:r]:
                l += s[l:r].index(s[r]) + 1
            elif r != l:
                l += 1
            elif r == l:
                r += 1
            if s[r] not in s[l:r] and r == len(s) - 1:
                summ = max(summ, r - l + 1)
        return summ
