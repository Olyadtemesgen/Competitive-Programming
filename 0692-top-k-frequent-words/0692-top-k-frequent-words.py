class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        array = Counter(words)
        ans = []
        for cc in array:
            ans.append([-array[cc], cc])
        
        heapq.heapify(ans)
        answer = []
        
        while k:
            answer.append(heapq.heappop(ans)[1])
            k -= 1
        
        return answer