class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        results = []
        for word in words:

            results.append(Counter(word))
        result = []

        for char in results[0]:
            
            returned = results[0][char]
            
            for dic in results[1:]:
                
                if char not in dic:
                    returned = 0
                    break    
                else:

                    returned = min(returned, dic[char])
        
            result += [char] * returned
        
        return result