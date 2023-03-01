class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        counter = Counter(s)

        stack = []

        for right in range(len(s)):
            
            if not stack:
                stack.append(s[right])
                
            
            elif s[right] not in stack: 
                    
                while stack and counter[stack[-1]] and s[right] < stack[-1]:

                    stack.pop()
                    
                stack.append(s[right])
            
            counter[s[right]] -= 1
        
        return "".join(stack)
                
        