class Solution:
    

    def reversePairs(self, nums: List[int]) -> int:
        
        answers = 0
        
        def mergeSort(left, right):
            
            nonlocal answers
            
            if left == right:
                return [nums[left]]

            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1, right)

            l = 0
            r = 0
            answer = []
            left1 = sorted(left_half)
            right1 = sorted(right_half)

            rights = 0
            for x in range(len(left1)):
                
                while rights < len(right1) and 2 * right1[rights] < left1[x]: 
                    
                    rights += 1
                
                answers += rights

            return left_half + right_half
        
        mergeSort(0, len(nums) - 1)
        
        return answers