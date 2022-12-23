class Solution:
    def freqAlphabets(self, s: str) -> str:
        queue = []
        result = ''
        length = len(s)

        for char in s:
            if char != '#':
                queue.append(char)
                if len(queue) == 3:
                    result += chr(int(queue.pop(0))+ 96)
            else:
                result += chr(int(queue.pop(-2) + queue.pop(-1)) + 96)
        #if there are integers left in the queue
        while queue:
            result += chr(int(queue.pop(0))+ 96)
        
        return result