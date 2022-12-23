class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]
        #this code consists of losers
        losers = []
        winners = set()
        for match in matches:
            losers.append(match[1])
            winners.add(match[0])
        answer[0] = sorted(list(winners.difference(set(losers))))
        counter = Counter(losers)
        for loser in counter:
            if counter[loser] == 1:
                answer[1].append(loser)
        answer[1].sort()
        return answer