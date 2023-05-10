class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        set_rec = set(recipes)
        set_sup = set(supplies)
        
        graph = defaultdict(list)
        
        queue = deque([])
        graph2 = defaultdict(int)
        
        for index in range(len(recipes)):
            
            aa = False
            for ind in range(len(ingredients[index])):
                
                if ingredients[index][ind] not in supplies and ingredients[index][ind] in set_rec:
                    graph[ingredients[index][ind]].append(recipes[index])
                    
                    graph2[recipes[index]] += 1
                    
                    aa = True
                
                elif ingredients[index][ind] not in supplies:
                    ingredients[index] = None
                    recipes[index] = None
                    aa = True
                    break
            
            if not aa:
                queue.append(recipes[index])
        
        answer = []
        while queue:
            
            value = queue.popleft()
            
            answer.append(value)
            
            for x in graph[value]:
                
                graph2[x] -= 1
                
                if graph2[x] == 0:
                    queue.append(x)
        
        return answer