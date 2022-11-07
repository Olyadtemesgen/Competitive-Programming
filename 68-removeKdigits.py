class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums) == k:return '0'
        stack = []
        for num in nums:
            while stack and k and stack[-1] > num:
                stack.pop()
                k -= 1
            if len(stack) == 1 and stack[-1] == '0':
                stack.pop()
            stack.append(num)
        while k and stack:
            stack.pop()
            k -= 1
        res = ''.join(stack)  
        return res if res != '' else '0'
