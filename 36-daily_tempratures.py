#this is the best solution I got
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [temperatures[0]]
        stack2 = [0]
        stack3 = [0] * len(temperatures)
        x = 1
        while x < len(temperatures):
            if not stack  or not stack2:
                stack.append(temperatures[x])
                stack2.append(x)
            elif stack[len(stack) - 1] >= temperatures[x]:
                    stack.append(temperatures[x])
                    stack2.append(x)
                    x += 1
            else:
                stack.pop()
                stack3[stack2[len(stack2) - 1]] = x - stack2[len(stack2) - 1]
                stack2.pop()
        stack3[len(temperatures) - 1] = 0
        return stack3
 #and this is the brute force solution'
class Solution:
    def dailyTemperatures(self, temperatures):
        result = []
        for x in range(len(temperatures)):
            for y in range(x + 1, len(temperatures)):
                if max(temperatures[x:]) == temperatures[x]:
                    result.append(0)
                    break
                if temperatures[x] < temperatures[y]:
                    result.append(y - x)
                    break
        result.append(0)
        return result
