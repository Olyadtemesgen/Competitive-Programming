aa = list(map(int, input().split()))

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

left = 0
right = 0

for x in range(len(array2)):
    while left < len(array1) and array1[left] < array2[x]:
        left += 1
    
    print(left, end=" ")
