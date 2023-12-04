class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxlen = 0

        for word in s:
            maxlen = max(maxlen, len(word))
        
        result = []   
        for index in range(maxlen):
            
            column = []
            flag = True
            
            for word in s:
                
                if index < len(word):
                    column.append(word[index]) 
                    flag = False
                
                else:
                    column.append(' ')
            
            column = ''.join(column)
            column = column.rstrip()
            result.append(column)
            
        return result