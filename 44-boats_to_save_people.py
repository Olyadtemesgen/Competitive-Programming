#this algorithm is my best coz I got 87 on time complexity and 75 on space complexity
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        left = 0
        right = len(people) - 1
        counter = 0
        while left <= right:
            if right == left:
                counter += 1
                break
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
                counter += 1
            elif people[left] + people[right] > limit:
                while people[left] + people[right] > limit and left < right:
                    right -= 1
                    counter += 1
        return counter
