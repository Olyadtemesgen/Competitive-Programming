t = int(input())

for test in range(t):
    n = int(input())
    array = sorted(map(int, input().split()))
    flag = False
    for index, num in enumerate(array[1:]):
        
        if num - array[index] > 1:
            print('NO')
            flag = True
            break
    if not flag:
        print('YES')
        
