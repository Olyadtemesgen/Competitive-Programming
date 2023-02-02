from collections import Counter, defaultdict


[n , m] = list(map(int, input().split()))
array = []
for a in range(n):
    array.append(input())

dict1 = []
for x in range(n):
    dict1.append(Counter(array[x]))
dicts = []

for x in range(m):
    aa = ""
    for y in range(n):
        aa += array[y][x]

    dicts.append(Counter(aa))
result = ''

for indexx, row in enumerate(array):
    for index, char in enumerate(row):
        
        if dict1[indexx][char] == 1 and dicts[index][char] == 1:
            result += char

print(result)
