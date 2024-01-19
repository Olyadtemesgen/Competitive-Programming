class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        chars = [0 for x in range(len(s))]
        
        for shift in shifts:
            
            if shift[2] == 1:
                
                chars[shift[0]] += 1
                
                if shift[1] < len(s) - 1:
                    chars[shift[1] + 1] -= 1
            else:
                chars[shift[0]] -= 1
                
                if shift[1] < len(s) - 1:
                    chars[shift[1] + 1] += 1
        
        for index in range(1, len(s)):
            chars[index] += chars[index - 1]
            chars[index] %= 26
        
        chars[0] %= 26
        
        
        otherres = []
        
        for index, char in enumerate(chars):
            
            if char > -1:
                characterr = (ord(s[index]) + char)
                
                if characterr > 122:
                    otherres.append(chr(96 + characterr - 122))
                
                else:
                    otherres.append(chr(characterr))
            
            else:
                characterr = (ord(s[index]) + char)
                if characterr < 97:
                    # consistency
                    what_a_flag = False
                    otherres.append(chr(123 - 97 + characterr))
                
                else:
                    otherres.append(chr(characterr))
        
        return "".join(otherres)
        