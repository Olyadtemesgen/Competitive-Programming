class Solution:
    
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        total = 0
        array = []

        for x in range(len(nums1)):
            nums1[x] -= nums2[x]

        def merger(left, right, array):
            
            nonlocal total

            if len(array) == 1:
                return array

            elif left >= right:
                return []

            mid = left + (right - left) // 2
            
            array2 = array[left:mid]
            
            lefter = merger(left, mid, array2)
            
            mid = left + (right - left) // 2
            array3 = array[mid:right]

            righter = merger(left, len(array) - mid, array3)

            leftt = 0
            rightt = 0

            result = []

            for number in righter:
                total += bisect.bisect_right(lefter,number + diff)
            
            while leftt < len(lefter) and rightt < len(righter):
                
                if lefter[leftt] <= righter[rightt]:
                    result.append(lefter[leftt])
                    leftt += 1
                
                else:
                    result.append(righter[rightt])
                    rightt += 1

            while leftt < len(lefter):
                result.append(lefter[leftt])
                leftt += 1
            
            while rightt < len(righter):
                result.append(righter[rightt])
                rightt += 1
            
            return result
        
        merger(0, len(nums1), nums1)
        
        return total