class Solution:
    def evalRPN(self, tokens):
        new = []
        for x in tokens:
            if ord(x[0]) >= 48 and ord(x[0]) <= 57 or (ord(x[0]) == 45 and len(x) > 1):
                new.append(int(x))
            elif x in '+-*/':
                if x == '+' : 
                    new[len(new) - 2:] = [(new[len(new) - 1] + new[len(new) - 2])]
                elif x == '-' : 
                    new[len(new) - 2:] = [(new[len(new) - 2] - new[len(new) - 1])]
                elif x == '*' : 
                    new[len(new) - 2:] = [ (new[len(new) - 1] * new[len(new) - 2])]
                elif x == '/' and new[len(new) - 1] != 0 :
                    new[len(new) - 2:] = [int(( new[len(new) - 2]) / new[len(new) - 1])]
        return new[len(new) - 1]
#It will become much simpler when we use stack
    def evalRPN(self, tokens):
        stack = []
        for x in tokens:
            if x == '+':
                stack.append(stack.pop() + stack.pop())
            elif x == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif x == '*':
                stack.append(stack.pop() * stack.pop())
            elif x == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(x))
        return int(stack[0])
