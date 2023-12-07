class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        right = len(num) - 1

        while right + 1 and not int(num[right]) % 2:
            right -= 1
        
        return num[:right + 1]