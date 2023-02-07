n = int(input())

array = list(map(int, input().split()))
"""dict_index = {}
for index, x in enumerate(array):
    dict_index[x] = index
for index in range(len(array)):
    minimum = array[index]
    min_index = index

    for index_1 in range(index + 1, len(array)):
        
        if (minimum + array[index_1]) % 2 and minimum > array[index_1]:
            min_index = index_1
            minimum = array[index_1]
        
    array[min_index], array[index] = array[index], array[min_index]

print(" ".join(list(map(str, array))))"""


count_even = 0
count_odd = 0
 
for point in array:
    if not point % 2:
        count_even += 1
    
    else:
        count_odd += 1
 
    if count_even > 0 and count_odd > 0:
        array.sort()
        print(*array)
        break

else:
    print(*array)
