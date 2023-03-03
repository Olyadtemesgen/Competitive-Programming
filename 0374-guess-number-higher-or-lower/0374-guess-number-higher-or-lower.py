# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if not guess(mid):
                return mid
            
            elif guess(mid) == 1:
                left = mid + 1
            
            else:
                right = mid - 1