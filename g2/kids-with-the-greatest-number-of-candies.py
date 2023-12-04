class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maximum = max(candies)

        answer = []

        for num in candies:
            answer.append(num + extraCandies >= maximum)
        
        return answer