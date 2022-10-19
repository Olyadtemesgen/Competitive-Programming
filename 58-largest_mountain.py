class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        right = 1
        result = 0
        while right < len(arr):
            pointer = right
            flag = False
            counter = 1
            while pointer < len(arr) and arr[pointer]  > arr[pointer - 1]:
                counter += 1
                pointer += 1
            while pointer != right and pointer < len(arr) and arr[pointer] < arr[pointer - 1]:
                flag = True
                counter += 1
                pointer += 1
            if right < pointer and counter > 2:
                result = max(result, counter)
            if right != pointer:
                right = pointer
            else:
                right += 1
        return result
