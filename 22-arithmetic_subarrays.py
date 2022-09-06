class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        new = []
        for lister in range(len(r)):
            new.append(nums[l[lister]:r[lister] +1])
        neww = []
        for lists in new:
            neww.append(sorted(lists))
        answer = []
        for others in neww:
            n = []
            num = others[1] - others[0]
            for y in range(1, len(others) - 1):
                if num == others[y + 1] - others[y]:
                    n.append(1)
            if len(n) == len(others) - 2:
                answer.append(True)
            else:
                answer.append(False)
        return answer
