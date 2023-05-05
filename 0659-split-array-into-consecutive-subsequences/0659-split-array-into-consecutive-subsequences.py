class Solution:
    
    def isPossible(self, nums: List[int]) -> bool:
            
        freq = Counter(nums)
        ends = defaultdict(int)

        for num in nums:
        
            if freq[num] == 0:
                continue

            if ends[num-1] > 0:
                freq[num] -= 1
                ends[num-1] -= 1
                ends[num] += 1

            elif freq[num+1] > 0 and freq[num+2] > 0:

                freq[num] -= 1
                freq[num+1] -= 1
                freq[num+2] -= 1
                ends[num+2] += 1

            else:
                return False

        return True