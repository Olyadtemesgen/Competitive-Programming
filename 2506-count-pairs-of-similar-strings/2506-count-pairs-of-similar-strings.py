class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        for x in range(len(words)):
            for y in range(x + 1, len(words)):
                if len(set(words[x])) == len(set(words[y])):
                    if sorted(set(words[x])) == sorted(set(words[y])):res += 1
        return res