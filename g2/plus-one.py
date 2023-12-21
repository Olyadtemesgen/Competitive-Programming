class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] == 9:
            
            right = len(digits) - 1
            
            while right + 1 and digits[right] == 9:
                right -= 1
            if not right + 1:
                for x in range(len(digits)):
                    if not x:
                        digits[x] = 1
                    else:
                        digits[x] = 0
                digits.append(0)
                return digits

            digits[right] += 1
            right += 1

            while right < len(digits):
                digits[right] = 0 
                right += 1
        
        else:
            digits[-1] += 1
        return digits