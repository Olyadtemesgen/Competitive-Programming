class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        
        result = [[] for x in range(numRows)]
        length = len(s)

        arr = 0
        idx = 0
        if numRows == 1:
            return s
        while arr < length:

            while arr < length and idx < numRows:
                result[idx].append(s[arr])
                arr += 1
                idx += 1
            
            idx -= 2

            while arr < length and idx >= 0:
                result[idx].append(s[arr])
                arr += 1
                idx -= 1
            idx = 1
        answer = ""
        for x in result:
            answer += "".join(x)
        
        return answer