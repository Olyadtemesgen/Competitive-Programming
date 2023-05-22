class DisjointSet:
    def __init__(self):

        self.parent = [chr(x) for x in range(97, 123)]
        self.rank = [1 for _ in range(26)]
    
    def find(self, ch1):
        
        if ch1 == self.parent[ord(ch1) - 97]:
            return ch1
        
        # self.parent[ord(ch1) - 97] = self.find(self.parent[ord(ch1) - 97])
        self.parent[ord(ch1) - 97] = self.find(self.parent[ord(ch1) - 97])
        
        return self.parent[ord(ch1) - 97]


    def union(self, ch1, ch2):
        
        ch1 = self.find(ch1)
        ch2 = self.find(ch2)
        
        
        if self.rank[(ord(ch1)) - 97] > self.rank[(ord(ch2)) - 97]:
            self.parent[(ord(ch1)) - 97] = ch2

        elif self.rank[(ord(ch1)) - 97] < self.rank[(ord(ch2)) - 97]:
            self.parent[(ord(ch2)) - 97] = ch1

        else:
            self.parent[(ord(ch1)) - 97] = ch2
            self.rank[(ord(ch2)) - 97] += 1
    
    def is_connected(self, ch1, ch2):
        return self.find(ch1) == self.find(ch2)


class Solution:
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        ds = DisjointSet()
        
        swap = {chr(i):chr(i) for i in range(97, 123)}
        
        for index in range(len(s1)):
            if not ds.is_connected(s1[index], s2[index]):
                ds.union(s1[index], s2[index])
        
        for ind1 in range(97, 123):
            for ind2 in range(97, ind1):
                if ds.is_connected(chr(ind1), chr(ind2)):
                    swap[chr(ind1)] = chr(ind2)
                    break
        
        answer = []
        
        for ss in baseStr:
            answer.append(swap[ss])
        
        return "".join(answer)