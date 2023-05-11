class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
    
        def minimax(left: int, right: int, score1: int, score2: int, is_player1: bool, alpha, beta) -> int:
            
            if left == right:
                return score1 + nums[left] if is_player1 else score2 + nums[left]
            
            if is_player1:
                v = float('-inf')
            
                for i in range(2):
                    if i == 0:
                        v = max(v, minimax(left+1, right, score1+nums[left], score2, False, alpha, beta))
                    else:
                        v = max(v, minimax(left, right-1, score1+nums[right], score2, False, alpha, beta))
                    alpha = max(alpha, v)

                    if alpha >= beta:
                        break

                return v
            else:
                v = float('inf')
                
                for i in range(2):
                    if i == 0:
                        v = min(v, minimax(left+1, right, score1, score2+nums[left], True, alpha, beta))
                    else:
                        v = min(v, minimax(left, right-1, score1, score2+nums[right], True, alpha, beta))
                    beta = min(beta, v)
                    if alpha >= beta:
                        break
                
                return v

        total_score = sum(nums)
        player1_score = minimax(0, len(nums)-1, 0, 0, True, float('-inf'), float('inf'))
        return player1_score >= (total_score - player1_score)
