class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        #find the minimum word
        min_word = min(len(word1), len(word2))

        for indexes in range(min_word):
            result += word1[indexes] + word2[indexes]

        if len(word1) > min_word:
            result += word1[min_word:]

        elif len(word2) > min_word:
            result += word2[min_word:]

        return result