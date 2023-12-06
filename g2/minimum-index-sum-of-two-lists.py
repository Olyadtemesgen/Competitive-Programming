class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        list1_with_index = [[list1[i], i] for i in range(len(list1))]
        list2_with_index = [[list2[i], i] for i in range(len(list2))]

        list1_with_index.sort()
        list2_with_index.sort()

        pointer1 = 0
        pointer2 = 0

        answer = defaultdict(list)
        while pointer1 < len(list1) and pointer2 < len(list2):
            
            while pointer1 < len(list1) and list1_with_index[pointer1][0] < list2_with_index[pointer2][0]:
                pointer1 += 1
            
            while pointer2 < len(list2) and pointer1 < len(list1) and   list1_with_index[pointer1][0] > list2_with_index[pointer2][0]:
                pointer2 += 1
            
            

            if pointer1 < len(list1) and pointer2 < len(list2) and list1_with_index[pointer1][0] == list2_with_index[pointer2][0]:
                
                answer[list1_with_index[pointer1][1] + list2_with_index[pointer2][1]].append(list1_with_index[pointer1][0])
            
                pointer1 += 1
                pointer2 += 1
        
        minimum = inf

        for i in answer:
            minimum = min(minimum, i)
        
        return answer[minimum]