class Solution:
    def pancakeSort(self, arr):
        k = []
        a = min(arr)
        x = len(arr)
        for ab in range(x):
            max_ = max(arr[:x - ab])
            indexm = arr.index(max_) + 1
            arr[:indexm] = reversed(arr[:indexm])
            k.append(indexm)
            arr[:x - ab] = reversed(arr[:x - ab])
            k.append(x - ab)
            if x - ab == 2 and arr[0] == a:
                break
        return k
