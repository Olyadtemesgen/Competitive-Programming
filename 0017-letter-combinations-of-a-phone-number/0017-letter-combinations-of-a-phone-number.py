class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        if not digits:
            return []
        
        if len(digits)== 1:
            return dictionary[digits[0]]
        
        result = []
        
        for cur in self.letterCombinations(digits[:len(digits) - 1]):
            
            for after in dictionary[digits[-1]]:
                result.append(cur + after)
        
        return result