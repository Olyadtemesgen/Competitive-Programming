class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''The algorithm works in such a way that
        it iterate through all indexes of each word 
        and by using the sorter hash map it finds 
        whether it is sorted or not in order eyes'''
        minimum = 1000
        #minimum is used to not make index out of range errors
        sorter = {order[0]:0}
        #sorter help us know the order of the aliens
        sort_number = 1
        
        length = len(words)
        #this is the edge case where all the words are the same we return True
        if len(set(words)) == 1:
            return True

        for char in order[1:]:
            sorter[char] = sort_number
            sort_number += 1
            
        for word in words:
            minimum = min(minimum, len(word))
        #Here is where the logic happen
        for index in range(minimum):
            
            id = 0
            for index_all in range(1, length):
                
                if sorter[words[index_all][index]] < sorter[words[index_all - 1][index]]:
                    return False
                
                elif sorter[words[index_all][index]] == sorter[words[index_all - 1][index]]:
                    id += 1
                    
                if index_all == length - 1 and not id:
                    return True
                    
        return len(words[1]) > len(words[0])
