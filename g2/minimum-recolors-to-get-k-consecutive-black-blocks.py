class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])
        a = counter['W']
        left = 0
        for right in range(k, len(blocks)):
            counter[blocks[left]] -= 1
            counter[blocks[right]] += 1
            a = min(counter['W'], a)
            left += 1
        return a