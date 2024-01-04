class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            index = (len(nums) + i + nums[i]) % len(nums)

            if index == i:
                continue
            sets = {i, index}

            before = 0
            starter = nums[i] >= 0

            
            while True:
                if nums[i] * nums[index] < 0:
                    break

                ii = index
                
                index = (index + nums[index]) % len(nums)
                
                index = (len(nums) + index) % len(nums)
                
                if ii == index or (nums[index] >= 0) ^ starter:
                    break
                
                if index in sets:
                    return True
                
                sets.add(index)
            
        return False