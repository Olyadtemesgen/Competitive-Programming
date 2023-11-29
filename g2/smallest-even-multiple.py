class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return [n, 2 * n][n % 2]