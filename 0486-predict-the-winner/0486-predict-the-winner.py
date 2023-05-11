class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def fn(left: int, right: int, score1: int, score2: int, is_player1: bool) -> int:
            if left == right:
                return score1 + nums[left] if is_player1 else score2 + nums[left]

            if is_player1:
                return max(fn(left+1, right, score1+nums[left], score2, False), 
                            fn(left, right-1, score1+nums[right], score2, False))

            else:
                return min(fn(left+1, right, score1, score2+nums[left], True), 
                            fn(left, right-1, score1, score2+nums[right], True))

        
        total_score = sum(nums)

                # memo = {}

        player1_score = fn(0, len(nums)-1, 0, 0, True)
        print(player1_score)
        return  player1_score >= (sum(nums) - player1_score)
    