class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        length = len(command)
        
        for index in range(1, length):
            if command[index] == ')':
                if command[index - 1] == '(':
                    result += 'o'
                else:
                    result += 'al'
            elif command[index - 1] == 'G':
                result += 'G'
        if command[length - 1] == 'G':
            result += 'G'
        return result