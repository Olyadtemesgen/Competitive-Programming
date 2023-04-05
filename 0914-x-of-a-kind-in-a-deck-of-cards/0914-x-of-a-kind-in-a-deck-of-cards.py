class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        
        counter = Counter(deck)
        
        for y in counter:
            answer = counter[y]
            break
        
        for x in counter:
            answer = gcd(answer, counter[x])
        
        return answer > 1