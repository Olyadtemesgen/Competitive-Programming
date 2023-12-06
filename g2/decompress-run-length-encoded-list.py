class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        numbers = defaultdict(int)

        index = 0
        answer = []

        while index * 2 + 1 < len(nums):
            answer.extend([nums[index * 2 + 1]] * (nums[index * 2]))
            index += 1

        return answer