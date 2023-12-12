class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        result = ''
        s = list(s)[::-1]
        for x in s:
            if x != ' ':
                stack.append(x)
            if stack and x == ' ':
                result += ''.join(stack[::-1]) + ' '
                stack = []
        result += ''.join(stack[::-1])
        r = len(result) - 1
        while result[r] == ' ':
            r -= 1
        return result[:r + 1]
                