class Solution:
    
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            
            if s[0] == "*":
                return 9    
            return 1
        
        
        if s[0] == "*":
            before, now = 1, 9
        
        else:
            before, now = 1, 1
        xx = 1
        for index in range(1, len(s)):
            
            number = 0
            
            if s[index] == "*":
                number = now * 9
                
                for num in range(1, 10):
                    
                    if s[index - 1] != "*":
                        if 11 <= int(s[index - 1] + str(num)) <= 26:
                            number += before
                        
                        else:
                            break
                    
                    else:              
                        number += (15) * before
                        break
            
            else:
                
                number = now
                
                if s[index] == "0":
                    if s[index - 1] == "*":
                        number = before * 2

                    elif int(s[index - 1]) >= 3 or s[index - 1] == "0":                        
                        return 0
                    else:
                        number = before
                
                elif s[index - 1] != "*":
                    if 11 <= int(s[index - 1] + s[index]) <= 26:
                        number += before
                
                else:
                    
                    if int(s[index]):
                        for nm in [1, 2]:
                            if nm * 10 + int(s[index]) <= 26:
                                number += before   

                            else:
                                break 

            xx = before
            before = now
            now = number
        
        return now % (10 ** 9 + 7)
