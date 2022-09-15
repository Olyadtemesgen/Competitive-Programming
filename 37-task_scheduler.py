from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        frequency = [value for value in counter.values()]
        max_ = max(frequency)
        marx_freq = frequency.count(max_)
        return max(len(tasks), (max_ - 1) * (n + 1) + marx_freq)
