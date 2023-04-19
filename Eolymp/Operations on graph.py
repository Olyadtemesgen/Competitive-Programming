n = int(input())
from collections import defaultdict
dict = defaultdict(list)
t = int(input())
for x in range(t):
    inp = list(map(int, input().split()))
    
    if inp[0] == 2:
        for x in dict[inp[1]]:
            print(x, end=" ")
    
    else:
        dict[inp[1]].append(inp[2])
        dict[inp[2]].append(inp[1])
