class Solution:
    def minimumSteps(self, s: str) -> int:
        black_point = len(s)

        answer = 0
        for right in range(len(s) - 1, -1, -1):
            if s[right] == "1" and black_point != right:
                answer += black_point - right - 1
                black_point -= 1
            
        return answer