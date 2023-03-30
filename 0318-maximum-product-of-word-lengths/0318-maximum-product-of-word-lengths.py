class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        
        saved = []
        
        for x in range(len(words)):
            
            saved.append(len(words[x]))
            
            words[x] = set(words[x])
            
        for index1 in range(len(words)):
            
            for index2 in range(index1 + 1, len(words)):
                
                if len(words[index1].union(words[index2])) == len(words[index1]) + len(words[index2]):
                    
                    answer = max(answer, saved[index1] * saved[index2])
            
        return answer