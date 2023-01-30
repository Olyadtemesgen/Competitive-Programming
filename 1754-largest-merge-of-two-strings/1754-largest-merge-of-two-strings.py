class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        minimum = min(len(word1), len(word2))
        pointer1 = 0
        pointer2 = 0
        merge = ''
        flag = False
        
        while not flag and pointer1 < len(word1) and pointer2 < len(word2):
            
            saver = pointer1
            saver2 = pointer2
            
            if word1[saver] == word2[saver2]:
                while saver < len(word1) and \
                saver2 < len(word2) and \
                word1[saver] == word2[saver2]:
                    saver += 1
                    saver2 += 1
                    
                if saver < len(word1) and saver2 < len(word2):
                    
                    if word1[saver] > word2[saver2]:
                        merge += word1[pointer1]
                        pointer1 += 1
                    
                    else:
                        merge += word2[pointer2]
                        pointer2 += 1
                
                else:
                    if pointer1 - len(word1) < pointer2 - len(word2):
                        merge += word1[pointer1]
                        pointer1 += 1
                    
                    else:
                        merge += word2[pointer2]
                        pointer2 += 1
                    
            elif word1[pointer1] > word2[pointer2]:
                merge += word1[pointer1]
                pointer1 += 1
                
            elif word1[pointer1] < word2[pointer2]:
                merge += word2[pointer2]
                pointer2 += 1
    
        if pointer1 != len(word1):
            merge += word1[pointer1:]
        
        if pointer2 != len(word2):
            merge += word2[pointer2:]
        
        return merge