class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        right = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and right < len(pushed) and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return not stack
            
