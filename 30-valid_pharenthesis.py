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
            

        if len(stack) == 0:
            return True 
        else:
            return False
