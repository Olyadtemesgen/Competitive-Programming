from collections import Counter
class Solution:
    def minSetSize(self, arr):
        counter = Counter(arr)
        new = []
        for x in counter:
            new.append(counter[x])
        su = 0
        countr = 0
        print(len(arr))
        new.sort(reverse=True)
        for ab in new:
            if su < len(arr) // 2:
                su += ab
                countr += 1
            else:
                break
        return countr
