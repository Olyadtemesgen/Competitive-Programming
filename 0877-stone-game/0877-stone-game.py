class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

#                 return max(min())?
#         prefix = [0, piles[0]]
#         for x in range(1, len(piles)):
#             prefix.append(prefix[-1] + piles[x])

        return True
#         def find_the_winner(left, right):
            
#             if left > right:
#                 return 0
            
#             elif left == right:
#                 return piles[left]
            
#             choice1 = piles[left] + min(find_the_winner(left + 2, right), find_the_winner(left + 1, right - 1))
            
#             choice2 = piles[right] + min(find_the_winner(left + 1, right - 1), find_the_winner(left, right - 2))
            
#             return max(choice1, choice2)
        
#         value = find_the_winner(0, len(piles) - 1)
#         total = sum(piles)
        
#         return value > total / 2
    