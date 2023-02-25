class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        string = ""
        
        for char in s:
            string += str(ord(char) - 96)
        
        while k:

            

            sum = 0
            
            for nums in string:
                sum += (int(nums))
            string = str(sum)
            num = sum
            
            k -= 1
        return num