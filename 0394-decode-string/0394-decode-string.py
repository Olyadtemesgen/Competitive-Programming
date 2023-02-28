class Solution:
    def decodeString(self, s: str) -> str:
        integer = []
        opener = []
        stack = []
        
        for index, char in enumerate(s):
            
            if char in '0123456789':
                
                if not integer:
                    integer.append(char)
                
                elif s[index - 1] in '0123456789':
                    integer[-1] += char

                else:integer.append(char)
            
            elif char == '[':
                opener.append(len(stack))
                stack.append(char)
            
            elif char != ']':
                stack.append(char)
            
            elif char == ']':

                stack[opener[-1]:] = stack[opener[-1] + 1:] * int(integer[-1])
                integer.pop()
                opener.pop()
        
        return "".join(stack)