class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = ""
        
        while num:
            
            ans = str(int(not num % 2)) + ans
            num //= 2
        print(ans)
        return int("0b" + ans, 2)