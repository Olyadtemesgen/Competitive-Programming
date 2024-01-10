class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        answers = {"T": 0, "F": 0}

        left = 0
        answer = 0
        
        for right in range(len(answerKey)):
            answers[answerKey[right]] += 1

            while min(answers["T"], answers["F"]) > k:
                answers[answerKey[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)
        
        return answer