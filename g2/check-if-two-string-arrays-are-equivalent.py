class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        index = 0
        
        first_i = 0
        second_i = 0
        f_c = 0
        s_c = 0

        while True:
            if f_c == len(word1[first_i]):
                first_i += 1
                f_c = 0
            
            if s_c == len(word2[second_i]):
                second_i += 1
                s_c = 0
            
            if first_i == len(word1) and second_i == len(word2):
                return True
            
            if first_i == len(word1) or second_i == len(word2):
                return False
                
            if word1[first_i][f_c] != word2[second_i][s_c]:
                return False
            
            f_c += 1
            s_c += 1
        
        return True

