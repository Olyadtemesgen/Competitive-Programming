class Solution:
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        dicts = defaultdict(int)
        
        length = len(nums)
        for right in nums:
            dicts[right] += 1
        
        arr = []
        for right in range(1, length + 1):
            if right not in dicts:
                arr.append(right)
        
        return arr