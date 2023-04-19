n = int(input())
array = []

for x in range(n):
    array.append(list(map(int, input().split())))

sources = []
sinks = []

for x in range(n):
    
    if not sum(array[x]):
        sources.append(x + 1)
    
for x in range(n):
    a = False
    for y in range(n):
        if array[y][x]:
            a = True
            break
    
    if not a:
        sinks.append(x + 1)
print(len(sinks), end=" ")
print(*sinks)
print(len(sources), end=" ")
print(*sources)
# print(value1)
