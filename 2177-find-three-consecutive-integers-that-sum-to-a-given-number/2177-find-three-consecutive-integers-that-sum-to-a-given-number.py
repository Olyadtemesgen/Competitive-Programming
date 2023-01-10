class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        result = num % 3
        
        if not result:
            num = num // 3
            return [num - 1, num, num + 1]
        
        return []