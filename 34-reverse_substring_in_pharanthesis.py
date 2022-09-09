#amazing program man
class Solution:
    def reverseParentheses(self, s):
        ss = list(s)
        stack1 = []
        stack2 = []
        for x in range(len(s)):
            if ss[x] == ')':
                if stack2[-1] == '(':
                    stack2.append(s[x])
                    x = len(stack2) - 1
                else:
                    stack2[stack1[-1]:] = reversed(stack2[stack1[-1] + 1:])
                    stack1.pop()
            else:
                if ss[x] == '(' and ss[x + 1] != ')':
                    stack1.append(len(stack2))
                    stack2.append(ss[x])
                elif ss[x] == '(' and ss[x + 1] == ')':
                    ss[x] = '0'
                    ss[x + 1] = '0'
                else:
                    stack2.append(ss[x])
        res = ""
        for x in stack2:
            if x not in '()' and x != '0':
                res += x
        return res
