n = int(input())

array = []

for ar in range(n):
    array.append(list(map(int, input().split())))


for x in range(n):
    arr = []
    for y in range(n):

        if array[x][y]:
            arr.append(y + 1)
    
    print(len(arr), *arr)
