class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        counter = {}
        maximum = len(cards) + 1
        for right in range(len(cards)):

            if cards[right] not in counter:

                counter[cards[right]] = right
            
            else:
                maximum = min(maximum,  right + 1 - counter[cards[right]])
                counter[cards[right]] = right
            
        
        return maximum if maximum != len(cards) + 1 else -1