class Solution:
    def isValid(self, s):
        a = ['{','[','(']
        b = ['}',']',')']
        ss = list(s)
        stack = []
        if len(ss) % 2 != 0:
            return False
        for x in range(len(s)):
            if x < len(s) - 1 and ss[x] in a and ss[x + 1] in b and a.index(ss[x]) != b.index(ss[x + 1]):
                return False
            if ss[x] not in b:
                stack.append(ss[x])
            elif len(stack) == 0 and ss[x] in b:
                return False
            elif ss[x] in b and a.index(stack[len(stack) - 1]) == b.index(ss[x]):
                stack.pop()
        return True if not stack else False
 #there is a simplest logic to solve this problem
    def isValid2(self, s):
        b = {'}':'{',']':'[',')':'('}
        ss = list(s)
        stack = []
        for x in s:
            if x in b:
                if stack and stack[-1] == b[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
