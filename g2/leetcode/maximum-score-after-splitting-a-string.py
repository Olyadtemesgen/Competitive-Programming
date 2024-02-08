class Solution:
    def maxScore(self, s: str) -> int:
        
        prefix = []

        zero = 0
        one = 0
        for right in s:
            zero += 1 - int(right)
            one += int(right)
            prefix.append([zero, one])
        
        print(prefix)
        answer = 0

        for right in range(1, len(s)):
            answer = max(answer, prefix[right - 1][0] +(prefix[len(s) -1][1] - prefix[right - 1][1]))
        
        return answer
        