class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        upper = math.floor(math.sqrt(c))

        if c == 0:
            return True
        for x in range(1, upper + 1):
            
            if math.sqrt(c - x ** 2) == math.floor(math.sqrt(c - x ** 2)):
                return True
        
        return False