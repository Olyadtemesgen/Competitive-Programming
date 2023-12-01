class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for index, num in enumerate(s):
            if not index:result += numbers[num]
            elif numbers[s[index - 1]] < numbers[s[index]]:
                result += numbers[num]
                while index and numbers[s[index - 1]] < numbers[s[index]]:
                    index -= 1
                    result -= 2 * numbers[s[index]]
            else:result += numbers[num]
        return result