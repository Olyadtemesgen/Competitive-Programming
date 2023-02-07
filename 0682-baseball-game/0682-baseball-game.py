class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = []
        oper = ""
        for operation in operations:
            
            if not operation in 'CD+':
                result.append(int(operation))
            
            elif operation == 'C':
                result.pop()
            
            elif operation == 'D':
                result.append(result[-1] * 2)
            
            elif operation == '+':           
                result.append(result[-1] + result[-2])
                  
        return sum(result)