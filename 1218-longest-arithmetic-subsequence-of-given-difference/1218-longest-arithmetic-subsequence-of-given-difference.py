class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        result = 0
        
        for val in arr:
            
            if val - difference in dp:
                dp[val] = dp[val - difference] + 1
            
            else:
                dp[val] = 1
            
            result = max(result, dp[val])
        
        return result