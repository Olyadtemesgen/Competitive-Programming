class Solution:
    def smallestNumber(self, num: int) -> int:
        num = list(str(num))
        if num[0] == '-':
            num[::] = num[1:]
            num.sort(reverse=True)
            x = 0
            while not int(num[x]):
                x += 1
            num[0], num[x] = num[x], num[0]
            return -1 * int("".join(num))
        else:
            num.sort()
            x = 0
            while x < len(num) - 1 and not int(num[x]):
                x += 1
            num[0], num[x] = num[x], num[0]
            return int("".join(num))