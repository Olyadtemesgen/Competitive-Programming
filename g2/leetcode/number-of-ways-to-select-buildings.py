class Solution:
    def numberOfWays(self, s: str) -> int:
        
        array = []
        zero = 0
        one = 0
        for i in s:

            zero += 1 - int(i)
            one += int(i)
            array.append([zero, one])
        
        answer = 0

        for i in range(1, len(s) - 1):
            
            if not int(s[i]):
                answer += array[i - 1][1] * (array[len(s) - 1][1] - array[i][1])
            
            else:
                answer += array[i - 1][0] * (array[len(s) - 1][0] - array[i][0])
        
        return answer