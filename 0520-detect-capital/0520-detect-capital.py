class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        arr1 = word[0]
        if len(word) == 1:
            return True
        
        arr2 = word[1]
        
        if ord(arr1) < 97 and ord(arr2) < 97:
            for right in range(len(word)):
                if ord(word[right]) >= 97:
                    return False
        
        elif ord(arr1) < 97 and ord(arr2) >= 97:
            for right in range(1, len(word)):
                if ord(word[right]) < 97:
                    return False
        
        elif ord(arr1) > 96:
            for right in range(len(word)):
                if ord(word[right]) < 97:
                    return False
        
        return True