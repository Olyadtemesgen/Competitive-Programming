class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        counter = defaultdict(list)
        original_counter = counter
        for index, num in enumerate(nums):
            counter[num].append(index)
        
        for operation in operations:
            
            iterated = counter[operation[0]]
            
            for index in iterated:
                nums[index] = operation[1]
                
            if not (operation[1] in counter):
                
                del counter[operation[0]]
                counter[operation[1]] = iterated
        
        return nums