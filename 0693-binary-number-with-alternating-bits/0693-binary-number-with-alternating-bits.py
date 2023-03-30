class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        saved = math.floor(math.log2(n)) + 1
    
        return (2 ** saved - 1 == (n ^ (n >> 1)))
        
    