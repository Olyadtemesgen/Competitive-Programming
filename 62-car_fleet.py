class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        res = []
        for x in range(len(position)):
            res.append([target - position[x], speed[x]])
        res.sort()
        stack = []
        for x, y in res:
            stack.append(x / y)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
