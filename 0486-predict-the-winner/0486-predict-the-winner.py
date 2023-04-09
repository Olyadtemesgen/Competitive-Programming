class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def find_the_winner(left, right):
            
            if left > right:
                return 0
            
            elif left == right:
                return nums[left]
            
            choice1 = nums[left] + min(find_the_winner(left + 2, right), find_the_winner(left + 1, right - 1))
            
            choice2 = nums[right] + min(find_the_winner(left + 1, right - 1), find_the_winner(left, right - 2))
            
            return max(choice1, choice2)
        
        value = find_the_winner(0, len(nums) - 1)
        total = sum(nums)
        
        return value >= total / 2