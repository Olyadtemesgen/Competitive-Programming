class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        is_reversed = nums[-1] < nums[0]
        self.result = -1
        is_tl = target <= nums[-1]
        self.already_seen = set()

        if target == nums[-1]:
            return len(nums) - 1

        def binary_value_search(left:int, right:int):
            mid = (left + right) // 2 
            
            mid_value = nums[mid]
            if mid_value == target:
                self.result = mid
                return
            
            if left > right or self.result != -1 or mid in self.already_seen:
                return
            
            self.already_seen.add(mid)
            if mid_value > target:   
                if is_tl:
                    if mid_value > nums[-1]:
                        binary_value_search(mid + 1, right)
                    else:
                        binary_value_search(left, mid - 1)
                else:
                    binary_value_search(left, mid - 1)

            elif mid_value < target:    
                
                if is_tl:
                    binary_value_search(mid + 1, right)
                    
                else:
                    if mid_value <= nums[-1]:
                        binary_value_search(left, mid - 1)
                    else:
                        binary_value_search(mid + 1, right)
                
            
        
        binary_value_search(0, len(nums)- 1)
        return self.result