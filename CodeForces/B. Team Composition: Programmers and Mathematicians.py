t = int(input())

for xx in range(t):
    answer = list(map(int, input().split()))
    print(min(min(answer), (answer[0] + answer[1]) // 4))
