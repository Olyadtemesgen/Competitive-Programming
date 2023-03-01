class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        dicts = {}
        for x in range(26):
            dicts[chr(97 + x)] = x
        
        
        first = ""
        
        for x in firstWord:
            first += str(dicts[x])
            
        
        second = ""
        
        for x in secondWord:
            second += str(dicts[x])
        
        third = ""
        
        for x in targetWord:
            third += str(dicts[x])
            
        return int(first) + int(second) == int(third)