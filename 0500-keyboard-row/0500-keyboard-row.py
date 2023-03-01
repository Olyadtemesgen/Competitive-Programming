class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        dicts = {1:"qwertyuiopQWERTYUIOP",
                2:"asdfghjklASDFGHJKL",
                3:"zxcvbnmZXCVBNM"}
        saved = 1
        result = []
        for string in words:
            
            for x in dicts:
                if string[0] in dicts[x]:
                    saved = x
                    break
                    
            flag = True
            for char in string:
                if char not in dicts[saved]:
                    flag = False
            
            if flag:
                result.append(string)
            
              
        return result