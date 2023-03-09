class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        string = "0"
        saved = ""
        def finder(number, strs):
            
            nonlocal saved
            if number == n - 1:
                saved = strs[k - 1]
                return
            
            rests = ""
            
            for x in range(len(strs) - 1, -1, -1):
                if strs[x] == "0":
                    rests = rests + "1" 
                else:
                    rests += "0"
            
            finder(number + 1, strs + "1" + rests)
        
        finder(0, string)
        
        return saved