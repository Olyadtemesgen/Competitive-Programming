from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        frequency = [value for value in counter.values()]
        max_ = max(frequency)
        marx_freq = frequency.count(max_)
        return max(len(tasks), (max_ - 1) * (n + 1) + marx_freq)
#We also can to solve the problem with heapqueue mainly max_heap
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks, n):
        result, heap = 0, []
        counter = Counter(tasks)
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        while heap:
            i, temp = 0, []
            while i <= n:
                result += 1
                if heap:
                    v, k = heapq.heappop(heap)
                    v += 1
                    if v < 0:
                        temp.append((v, k))
                if not heap and not temp:
                    break
                i += 1
            for k, v in temp:
                heapq.heappush(heap, (k, v))
        return result
