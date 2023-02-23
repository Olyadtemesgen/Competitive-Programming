class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left = 0
        
        right = 0
        count = 0
        counter = defaultdict(int)
        result = 0
        
        for right in range(len(nums)):
            
            counter[nums[right]] += 1
            
            if len(counter) == k:

                count = 0
                saved = left
                
                cc = counter.copy()
                ll = left
                
                while left <= right and len(counter) == k:
                    
                    counter[nums[left]] -= 1
                    
                    if not counter[nums[left]]:
                        del counter[nums[left]]
                    
                    
                    left += 1
                    count += 1
                
                counter = cc
                left = ll

            elif len(counter) > k:
                
                count = 0
                
                while left <= right and len(counter) > k:
                    counter[nums[left]] -= 1
                    
                    if not counter[nums[left]]:
                        del counter[nums[left]]
                    
                    left += 1
                    

                if len(counter) == k:
    
                    count = 0
                    cc = counter.copy()
                    ll = left

                    while left <= right and len(counter) == k:
                        
                        counter[nums[left]] -= 1
                        count += 1
                        
                        if not counter[nums[left]]:
                            del counter[nums[left]]
                        
                        left += 1
                    
                    counter = cc
                    left = ll
            result += count
        
        return result