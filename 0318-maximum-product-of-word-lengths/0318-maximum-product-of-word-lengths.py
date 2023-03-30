class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        #by using bitmask
        
        array = []
        answer = 0
        
        for inx in range(len(words)):
            
            innumber = 0
            
            for word in words[inx]:
                innumber |= 1 << (ord(word) - ord('a'))
            
            for index in range(inx):
                
                if not (array[index] & innumber):
                    answer = max(answer, len(words[index]) * len(words[inx]))
            
            array.append(innumber)
        
        return answer