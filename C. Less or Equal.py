[n, k] = list(map(int, input().split()))

array = sorted(list(map(int, input().split())))

if k and k != n:
    k -= 1

    if array[k] != array[k + 1]:
        print(array[k])
    else:
        print(-1)
elif k == n:
    print(array[k - 1])

elif not k:
    if array[k] == 1:
        print(-1)
    else:
        print(1)

