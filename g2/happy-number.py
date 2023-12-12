class Solution:
    def isHappy(self, n: int) -> bool:
        for x in range(10):
            result = 0
            while n:
                result = result +(n%10)**2
                n = n // 10
            n = result
            if n == 1:return True
        return False