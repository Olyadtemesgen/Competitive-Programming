class Solution:
    def addDigits(self, num: int) -> int:
        
        while True:
            
            if num < 10:
                return num
            
            stri = str(num)
            
            sum = 0
            for nums in stri:
                sum += int(nums)
            
            num = sum
            