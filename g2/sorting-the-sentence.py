class Solution(object):
    def sortSentence(self, s):
        new_a = ""
        b = s.split()
        tester = '123456789'
        real = tester[:len(b)]
        for x in real:
            for y in b:
                if y.endswith(x):
                    if x != real[len(real) - 1]:
                        new_a += y[:len(y) - 1] + ' '
                    else:
                        new_a += y[:len(y) - 1]
        return new_a