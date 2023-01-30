class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        result = ''
        for word in dictionary:
            
            length = 0
            left = 0
            
            for char in s:
                
                if word[left] == char:
                    left += 1
                
                if left == len(word):
                    
                    if len(result) < len(word):
                        result = word
                        
                    elif len(result) == len(word) and word < result:
                        result = word
                    break
            
        return result