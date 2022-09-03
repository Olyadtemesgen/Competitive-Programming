def countingSort(arr):
    new_a = [0] * 100
    for x in arr:
        new_a[x] += 1
    return new_a
