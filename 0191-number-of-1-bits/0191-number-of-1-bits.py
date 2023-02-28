class Solution:
    def hammingWeight(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        elif n == 0:
            return 0
        
        if n % 2:
            return self.hammingWeight(n // 2) + 1
        else:
            return self.hammingWeight(n // 2)