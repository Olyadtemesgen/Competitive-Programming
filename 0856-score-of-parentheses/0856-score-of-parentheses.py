class Solution:
    
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        result = 0
        right = 0
        
        while right < len(s):

            if len(stack) == 1 and stack[0] != "(":
                result += stack.pop()
            
            lengths = len(stack) - 1

            while lengths > 1 and stack[lengths] != "(" and stack[lengths - 1] != "(":
                value = stack.pop()
                stack[-1] += value
                lengths -= 1

            if s[right] == "(":
                stack.append(s[right])
            
            else:
                if stack[-1] == "(":
                    stack[-1] = 1
                    length = len(stack) - 1
                    
                    while length > 1 and stack[length - 1] != "(":
                        value = stack.pop()
                        stack[-1] += value
                        length -= 1
                    
                else:
                    value = stack.pop()
                    stack[-1] = value * 2
            
            right += 1
        
        while stack:
            result += stack.pop()

        return result
                