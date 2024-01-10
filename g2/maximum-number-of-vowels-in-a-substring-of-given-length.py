class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        answer = 0
        ans = 0
        while left < len(s):
            aa = []
            while right - left < k:
                if right < len(s) and s[right] in 'aeiou':
                    ans += 1
                    aa.append(right)
                right += 1
            answer = max(answer, ans)
            if s[left] in 'aeiou':
                ans -= 1
            left += 1
        return answer