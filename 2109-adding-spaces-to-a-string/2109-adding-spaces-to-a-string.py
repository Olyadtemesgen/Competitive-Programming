class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        result = s[:spaces[0]]
        
        for x in range(1, len(spaces)):
            result += ' ' + s[spaces[x - 1]:spaces[x]]
            
        result += ' ' + s[spaces[-1]:]
        return result
    