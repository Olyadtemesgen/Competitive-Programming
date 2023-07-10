class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_right_dec = [0] * len(values)
        
        max_right_dec[-1] = values[-1] - len(values) + 1
        
        for index in range(len(values) - 2, -1, -1):
            max_right_dec[index] = max(max_right_dec[index + 1], values[index] - index)
        
        answer = 0
        
        for index in range(len(values) - 1):
            
            answer = max(answer, values[index] + index + max_right_dec[index + 1])
        
        return answer