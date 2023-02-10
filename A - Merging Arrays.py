a = input().split()
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

point_1 = 0
point_2 = 0

while point_1 < len(array1) and point_2 < len(array2):
    
    if array1[point_1] <= array2[point_2]:
        print(array1[point_1], end=" ")
        point_1 += 1
    
    else:
        print(array2[point_2], end=" ")
        point_2 += 1

while point_1 < len(array1):
    print(array1[point_1], end=" ")
    point_1 += 1

while point_2 < len(array2):
    print(array2[point_2], end=" ")
    point_2 += 1
