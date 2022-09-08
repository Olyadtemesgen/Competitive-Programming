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
