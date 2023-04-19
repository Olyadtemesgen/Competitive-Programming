n = int(input())
answer = []

for x in range(n):
    answer.append(list(map(int, input().split())))
ans = 0

for index1 in range(n):
    for index2 in range(n):
        ans += answer[index1][index2]
        answer[index2][index1] = 0

print(ans)
