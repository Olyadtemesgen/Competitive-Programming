class Solution:
    def PredictTheWinner(self, nums) -> bool:
        
        left, right = 0, len(nums) - 1
        
        def fn(left, right, turn, score_brook, score_oliad):
            if left > right:
                return score_brook >= score_oliad
            
            if turn:
                return fn(left + 1, right, 1 - turn, score_brook + nums[left], score_oliad) or fn(left, right - 1, 1 - turn, score_brook + nums[right], score_oliad)
            
            return fn(left + 1, right, 1 - turn, score_brook, score_oliad + nums[left]) and fn(left, right - 1, 1 - turn, score_brook, score_oliad + nums[right])
        
        return fn(left, right, 1, 0, 0)
            