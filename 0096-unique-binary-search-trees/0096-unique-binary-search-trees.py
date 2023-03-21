class Solution:
    
    def numTrees(self, n: int) -> int:
        
        dp = [1 for x in range(n + 1)]
        
        for node in range(2, n + 1):
            
            sub_answer = 0
            for root in range(1, node + 1):
                
                left = root - 1
                
                right = node - root
                
                sub_answer += (dp[left] * dp[right])
            
            dp[node] = sub_answer
        
        return dp[n]