class Solution:
    def splitString(self, s: str) -> bool:
        
        
        result = []
        isTrue = False
        
        if len(s) != 1 and len(set(s)) == 1:
            return False
        
        def splitter(result, index, isTrue):
            
            if index == len(s) - 1:
                return False
            if index == len(s):
                return False
            
            result.append(int(s[:index + 1]))
            
            string = ""
            for right in range(index + 1, len(s)):
                
                string += s[right]
                
                if  result[-1] - int(string) == 1:
                    
                    result.append(int(string))
                    string = ""
                    
            if not string or (int(str(result[-1]) + string) == result[-1]):
                return True

            else:
                return splitter([], index + 1, isTrue)
        
        aa = splitter(result, 0, False)
        return aa        