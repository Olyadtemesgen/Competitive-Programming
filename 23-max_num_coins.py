class Solution:
    def maxCoins(self, piles):
        piles.sort()
        length = len(piles) - 2
        sum = 0
        while length >= len(piles)//3:
            sum += piles[length]
            length -= 2
        return sum
