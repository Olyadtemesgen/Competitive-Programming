class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        
        for w in range(len(words)):
            words[w] = words[w].count(min(words[w]))
        
        words.sort()
        answer = []
        
        for query in queries:
            saved = query.count(min(query))
            ss = False
            
            answer.append(len(words) - bisect_right(words, saved))
            
        
        return answer