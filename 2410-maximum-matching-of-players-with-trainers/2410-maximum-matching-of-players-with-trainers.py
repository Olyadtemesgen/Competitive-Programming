class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        player = 0
        trainer = 0
        answer = 0

        while player < len(players) and trainer < len(trainers):

            while trainer < len(trainers) and trainers[trainer] < players[player]:
                trainer += 1

            if trainer < len(trainers):
                answer += 1
                trainer += 1
            
            player += 1
        
        return answer
