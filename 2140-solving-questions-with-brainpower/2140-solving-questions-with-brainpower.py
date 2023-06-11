class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
        
        def dp(index):
            
            if index in memo:
                return memo[index]
            
            if index >= len(questions):
                
                return 0
            if index == len(questions) - 1:
                return questions[index][0]
            
            memo[index] = max(dp(index + questions[index][1] + 1) + questions[index][0] , dp(index + 1))
            return memo[index]
            
        return dp(0)
